from odoo import models, fields, api
#crear por separado siempre
class Course(models.Model):
    _name = 'open_academy.course' #nombre del modelo
    name = fields.Char(string="titulo", required=True) #estos son mis campos
    description = fields.Text(string="descripcion")
    fecha = fields.Date(string="Fecha", required=True)
    #write y crete metodos en odoo, create registro en el metodo hacer la validacion
    # 
    responsable= fields.Many2one("res.users", string="responsable")
    sesiones= fields.One2many("open_academy.sesion", "curso",string="sesiones")