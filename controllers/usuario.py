#!/usr/bin/env python
#!-*- encoding:utf-8 -*-

def index():
    # redirect(URL(c='usuario', f='inicio', args=request.args, vars=request.vars))
    TicketComment.ticket_id.default = 2
    return dict(form=crud.create(TicketComment))


@auth.requires_login()
def inicio():
    user = auth.user

    systickets = None
    # Fields grid ticket
    fields = [Ticket.asunto, Ticket.turno_respuesta, Ticket.departamento]
    # Le mostramos al usuario los tickets que el creó en el sistema.
    query = Ticket.created_by == user.id

    if 'view' in request.args:
        from plugin_ticket import view_comment_ticket
        systickets = view_comment_ticket(request.args[-1])

    grid = SQLFORM.grid(query,
                        fields=fields,
                        searchable=False,
                        deletable=False,
                        csv=False)
    return dict(user=user, ticket=grid, systickets=systickets)



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