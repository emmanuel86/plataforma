@auth.requires_login()
def inicio():
    user = db(db.auth_user.id == session.auth.user.id).select(db.auth_user.first_name,
                                                            db.auth_user.last_name,
                                                            db.auth_user.email).first()
    
    fields = [db.ticket.user_id]
    grid = SQLFORM.grid(db.ticket,
                        searchable=False,
                        deletable=False,
                        csv=False,
                        fields=fields,
                        create=True)
    return dict(user=user, ticket=grid)

def servicios():
	return dict()

def soporte():
	grid = SQLFORM.grid(db.ticket,
                        searchable=False,
                        deletable=False,
                        csv=False,
                        create=True)
	return dict(ticket=grid)


def perfil():
	return dict()