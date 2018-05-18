# -*- coding: utf-8 -*-

def set_site(app):
    from app.models.site import SiteMeta
    metas = SiteMeta.all()
    metas = dict([(meta.name, meta.value) for meta in metas])
    app.site = metas


def load_site(app):
    with app.app_context():
        set_site(app)

        def site_context_processor():
            return dict(site=app.site)

        app.context_processor(site_context_processor)