# Obtenemos el total del IVA al 21% de la factura
# Propiedades: Solo lectura / Activar el seguimiento de pedidos: 100 / Lista negra en formularios web
# Nombre del campo: x_studio_total_iva_21_fra
# Dependencia
for record in self:
    total_21 = 0.0
    nombres_validos_21 = ['21% G', '21% IG', '21% S']
    
    for line in record.invoice_line_ids:
        # Obtenemos los impuestos de la línea
        impuestos = line.tax_ids
        if not impuestos:
            continue
            
        # Preguntamos a Odoo el desglose exacto
        # price_unit es el precio unitario sin impuestos
        res = impuestos.compute_all(
            line.price_unit, 
            quantity=line.quantity, 
            currency=line.currency_id, 
            product=line.product_id, 
            partner=line.partner_id
        )
        
        # Buscamos en el resultado si aparece alguno de nuestros impuestos
        for tax_res in res.get('taxes', []):
            if tax_res['name'] in nombres_validos_21:
                # Sumamos solo el importe de ESE impuesto específico
                total_21 += tax_res['amount']

    record['x_studio_total_iva_21_fra'] = total_21
