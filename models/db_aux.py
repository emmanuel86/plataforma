#!/usr/bin/env python
#-*- encoding:utf-8 -*-


if db(db.auth_group.role.like('tickets_%')).isempty():
    # Inicialización de los bases:
    #   * tickets_user
    #   * tickets_admin
    #   * tickets_soporte
    db.auth_group.insert(role='tickets_user',
                         description='Funciones básicas de tickets (crud)')
    db.auth_group.insert(role='tickets_admin',
                         description='Funciones de avanzadas de tickets')
    db.auth_group.insert(role='tickets_sporte',
                         description='Funciones intermedias de tickets')


#Funciones para cambiar el widget de buscar por codigo

def search_form(self,url):
    form = FORM(INPUT(_name='keywords', _style='width:200px;', _id='keywords'),
        INPUT(_type='submit',_value=T('Search')), 
        INPUT(_type='submit',_value=T('Clear'), 
        _onclick="jQuery('#keywords').val('');"), 
        _method="GET",_action=url) 
    return form


def search_query(tableid,search_text,fields): 
    words= search_text.split(' ') if search_text else [] 
    query=tableid<0#empty query 
    for field in fields: 
        new_query=tableid>0 
        for word in words: 
            new_query=new_query&field.contains(word)
        query=query|new_query 
    return query
#Fin de las funciones


def get_name(user):
    if user.first_name:
        return '%s, %s' % (user.first_name, user.last_name)
    else: return 'anonymus'