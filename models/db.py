# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])


## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

Userinfo = db.define_table('info_user_adicional',
                Field('user_id', db.auth_user),
                Field('imagen', 'upload'),
                Field('dni'),
                Field('email2'),
                Field('sexo', 'list:string'),
                Field('ocupacion'),
                Field('pais'),
                Field('provincia'),
                Field('ciudad'),
                Field('domicilio'),
                Field('codigo_postal'),
                Field('telefono')
                )



Forma_Pago = db.define_table('forma_pago',
            Field('descripcion'),
            format='%(descripcion)s'
    )

Servicio = db.define_table('servicio',
            Field('nombre'),
            Field('descripcion', 'text'),
            Field('precio', 'decimal(8, 2)'),
            format='%(nombre)s'
    )

Periodo = db.define_table('periodo',
            Field('descripcion'),
            format='%(descripcion)s'
    )

EstadoServicio = db.define_table('estado_servicio',
            Field('descripcion'),
            format='%(descripcion)s'
    )


User_Servicio = db.define_table('user_servicio',
            Field('user_id', db.auth_user),
            Field('nombre', unique=True),
            Field('servicio_id', Servicio),
            Field('periodo_id', Periodo),
            Field('forma_pago_id', Forma_Pago),
            Field('fecha_vencimiento', 'date'),
            Field('estado_id', EstadoServicio),
            auth.signature,
            format='%(servicio_id)s'
    )


Ticket = db.define_table('ticket',
                Field('asunto'),
                Field('user_servicio_id', User_Servicio),
                Field('departamento', 'reference auth_group'), # Mostar únicamente los que comienzan con tickets_
                Field('consulta', 'text'),
                Field('turno_respuesta', 'boolean'), # True side server - False side client
                Field('estado', 'boolean', default=True), # True: Abierto - False: Cerrado
                auth.signature,
                format='%(asunto)s'
                )


TicketComment = db.define_table('ticket_comment',
                        Field('ticket_id', Ticket),
                        Field('cuerpo', 'text'),
                        auth.signature,
                        format='%(ticket_id)s'
                )
