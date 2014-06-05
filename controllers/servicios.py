# Funciones
# Anular Pedido si el estado es igual a 1 (Pendiente)
def btn_anular_pedido(row):
    btn = ''
    if row.estado_id == 1:
        btn = A(I(_class='icon-thumbs-down'),
                    ' Anular Pedido',
                    _href=URL(c='servicios', 
                              f='anular_pedido',
                              args=[row.id],
                              user_signature=True),
                    _class='btn')
    return btn

# Boton Pagar
def btn_pagar(row):
    btn = A(I(_class='icon-thumbs-up'),
                ' Pagar',
                _href=URL(c='servicios',
                          f='pagar',
                          args=[row.id]),
                _class='btn')
    return btn



# Codigo
@auth.requires_login()
def index():
    user = auth.user
    query = User_Servicio.created_by == user.id
    fields = [User_Servicio.nombre,
                User_Servicio.servicio_id,
                User_Servicio.periodo_id,
                User_Servicio.forma_pago_id,
                User_Servicio.fecha_vencimiento,
                User_Servicio.estado_id,
                ]

    grid = SQLFORM.grid(query,
                    fields=fields,
                    create=False,
                    editable=False,
                    deletable=False,
                    details=False,
                    searchable=False,
                    user_signature=True,
                    csv=False,
                    links=[lambda r: btn_anular_pedido(r),
                            lambda r: btn_pagar(r)])
                    #orderby=User_Servicio.fecha_vencimiento)
            
    return dict(user=user, grid=grid)

def comprar():
    user = auth.user
    query = User_Servicio.created_by == user.id
    if 'comprar' in request.function:
        User_Servicio.user_id.default = user.id
        User_Servicio.user_id.writable = False
        User_Servicio.user_id.readable = False
        User_Servicio.estado_id.default = 1
        User_Servicio.estado_id.writable = False
        User_Servicio.estado_id.readable = False
        User_Servicio.fecha_vencimiento.default = request.now
        User_Servicio.fecha_vencimiento.writable = False
        User_Servicio.fecha_vencimiento.readable = False
    formulario = SQLFORM(User_Servicio)
    if formulario.process().accepted:
        response.flash = 'pedido enviado.'
    elif formulario.errors:
        response.flash = 'el pedido tiene errores.'
    else:
        response.flash = 'por favor complete el formulario.'
    return dict(formulario=formulario)

def pagar():
    return dict()


@auth.requires_signature()
def anular_pedido():
    anular = crud.delete(User_Servicio,
                        request.args[0],
                        message='Pedido Anulado',
                        next=URL(c='servicios', f='index'))
    return dict(crud=anular)