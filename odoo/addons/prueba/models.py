from odoo import api, models, fields

class Cliente(models.Model):
    _name = 'prueba.cliente'
    nombre = fields.Char()
    fecha_inscripcion = fields.Date(required=True)
    cod_mascotas = fields.One2many(comodel_name='prueba.mascota', inverse_name='cod_cliente')
    edad = fields.Integer(required=True);
    
    @api.constrains('edad','nombre')
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError('El cliente ' + record.nombre + ' debe ser mayor de edad, ya que tiene'+ str(record.edad) +' años.')
            else:
                pass

class Mascota(models.Model):
    _name = 'prueba.mascota'
    nombre = fields.Char()
    tipo = fields.Char()
    cod_cliente = fields.Many2one(comodel_name='prueba.cliente', inverse_name='cod_mascotas')