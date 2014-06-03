#!/usr/bin/env python
#!-*- encoding:utf-8 -*-

from gluon import current
from gluon.html import TAG, TABLE, TH, TR, TD


def view_comment_ticket(ticket_id):
    # Table TicketComment
    db = current.globalenv.get('db')
    crud = current.globalenv.get('crud')
    TicketComment = current.globalenv.get('TicketComment')

    query = TicketComment.is_active == True
    query &= TicketComment.ticket_id == ticket_id
    comments = db(query).select(orderby=TicketComment.created_on)

    # ticket default
    TicketComment.ticket_id.default = ticket_id
    form = crud.create(TicketComment)

    return TAG[''](comments, form)





