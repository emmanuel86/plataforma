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
                        create=True)
    return dict(user=user, ticket=grid)

def servicios():
    grid = SQLFORM.grid(Servicio,
                    editable=False,
                    deletable=False,
                    csv=False,)
    return dict(grid=grid)

def soporte():
	grid = SQLFORM.grid(db.ticket,
                        searchable=False,
                        deletable=False,
                        csv=False,
                        create=True)
	return dict(ticket=grid)


def perfil():
	return dict()