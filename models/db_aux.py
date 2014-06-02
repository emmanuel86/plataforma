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