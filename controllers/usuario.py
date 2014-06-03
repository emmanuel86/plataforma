def default():
    redirect(URL(c='usuario', f='inicio', args=request.args, vars=request.vars))

@auth.requires_login()
def inicio():
    user = auth.user

    # Le mostramos al usuario los tickets que el creó en el sistema.
    query = Ticket.created_by == user.id

    grid = SQLFORM.grid(query,
                        searchable=False,
                        deletable=False,
                        csv=False,
                        create=True,)
    return dict(user=user, ticket=grid)


@auth.requires_login()
def servicios():
    user = auth.user
    query = User_Servicio.created_by == user.id
    fields = [User_Servicio.servicio_id,
                User_Servicio.periodo_id,
                User_Servicio.forma_pago_id,
                User_Servicio.fecha_vencimiento,
                User_Servicio.estado_id,
                ]

    if 'new' in request.args:
        User_Servicio.user_id.default = user.id
        User_Servicio.user_id.writable = False
        User_Servicio.user_id.readable = False
        User_Servicio.estado_id.default = 1
        User_Servicio.estado_id.writable = False
        User_Servicio.estado_id.readable = False

    grid = SQLFORM.grid(query,
                    fields=fields,
                    create=True,
                    editable=False,
                    deletable=False,
                    searchable=False,
                    csv=False)
                    #orderby=User_Servicio.fecha_vencimiento)
            
    return dict(user=user, grid=grid)

def soporte():
	grid = SQLFORM.grid(db.ticket,
                        searchable=False,
                        deletable=False,
                        csv=False,
                        create=True)
	return dict(ticket=grid)


def perfil():
	return dict()