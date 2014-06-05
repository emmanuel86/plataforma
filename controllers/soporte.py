#!/usr/bin/env python
#-*- encoding:utf-8 -*-

def index():

    user = auth.user  # Usuario
    fields = [Ticket.asunto, Ticket.turno_respuesta, Ticket.departamento]
    query = Ticket.created_by == user.id  # Tickets del usuario.
    viewargs = None

    if request.vars.get('type') == 'cerrados':
        query &= Ticket.estado == False
    else: query &= Ticket.estado == True

    if 'view' in request.args:
        viewargs = {'comment_ticket': view_comment_ticket}

    grid = SQLFORM.grid(query,
                        fields=fields,
                        editable=False,
                        viewargs=viewargs,
                        csv=False)

    return dict(grid=grid)



def view_comment_ticket(ticket_id):
    query = TicketComment.is_active == True
    query &= TicketComment.ticket_id == ticket_id
    comments = db(query)
    
    TicketComment.ticket_id.default = ticket_id  # ticket default
    form = crud.create(TicketComment)

    if comments.count():
        trs = list()
        for comment in comments.select(orderby=~TicketComment.created_on):
            row = [TD(SPAN(get_name(comment.created_by),
                   BR()),
                   SPAN(prettydate(comment.created_on)), _class='span3'),
                   TD(SPAN(comment.cuerpo))]
            trs.append(TR(*row))
        table = TABLE(TBODY(*trs), _class='table table-striped table-condensed')
    else:
        table = SPAN('No hay comentarios')


    return TAG[''](table, form)