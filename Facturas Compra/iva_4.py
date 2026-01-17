# Obtenemos el total del IVA al 4% de la factura
# Propiedades: Solo lectura / Activar el seguimiento de pedidos: 100 / Lista negra en formularios web
# Nombre del campo: x_studio_iva_4_total_fra
# Dependencia
for record in self:
    total_4 = 0.0
    nombres_validos_4 = ['4% G', '4% IG', '4% S']
    
    for line in record.invoice_line_ids:
        impuestos = line.tax_ids
        if not impuestos:
            continue

        res = impuestos.compute_all(
            line.price_unit, 
            quantity=line.quantity, 
            currency=line.currency_id, 
            product=line.product_id, 
            partner=line.partner_id
        )
        
        for tax_res in res.get('taxes', []):
            if tax_res['name'] in nombres_validos_4:
                total_4 += tax_res['amount']

    record['x_studio_iva_4_total_fra'] = total_4
