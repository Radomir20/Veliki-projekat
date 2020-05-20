from django.urls import path
from . import views
from  django.conf.urls import url

urlpatterns = [
    path('Početna', views.pocetna, name='pocetna'),
    path('Asortiman', views.asortiman, name='asortiman'),
    path('Kako_do_nas', views.kako, name='kako'),
    path('Muškarci', views.muskarci, name='muskarci'),
    path('Žene', views.zene, name='zene'),
    path('Djeca', views.djeca, name='djeca'),
    url(r'^Muška_odjeća $', views.m_odjeca, name='m_odjeca'),
    url(r'^Muška_obuća $', views.m_obuca, name='m_obuca'),
    url(r'^Muška_oprema $', views.m_oprema, name='m_oprema'),
    url(r'^Ženska_odjeća $', views.z_odjeca, name='z_odjeca'),
    url(r'^Ženska_obuća $', views.z_obuca, name='z_obuca'),
    url(r'^Ženska_oprema $', views.z_oprema, name='z_oprema'),
    url(r'^Dječija_odjeća $', views.d_odjeca, name='d_odjeca'),
    url(r'^Dječija_obuća $', views.d_obuca, name='d_obuca'),
    url(r'^Dječija_oprema $', views.d_oprema, name='d_oprema'),
    url(r'^Muška_odjeća/(?P<m_odjeca_id>[0-9]+)/$', views.md_odjeca, name='md_odjeca'),
    url(r'^Muška_obuća/(?P<m_obuca_id>[0-9]+)/$', views.md_obuca, name='md_obuca'),
    url(r'^Muška_oprema/(?P<m_oprema_id>[0-9]+)/$', views.md_oprema, name='md_oprema'),
    url(r'^Ženska_odjeća/(?P<z_odjeca_id>[0-9]+)/$', views.zd_odjeca, name='zd_odjeca'),
    url(r'^Ženska_obuća/(?P<z_obuca_id>[0-9]+)/$', views.zd_obuca, name='zd_obuca'),
    url(r'^Ženska_oprema/(?P<z_oprema_id>[0-9]+)/$', views.zd_oprema, name='zd_oprema'),
    url(r'^Dječija_odjeća/(?P<d_odjeca_id>[0-9]+)/$', views.dd_odjeca, name='dd_odjeca'),
    url(r'^Dječija_obuća/(?P<d_obuca_id>[0-9]+)/$', views.dd_obuca, name='dd_obuca'),
    url(r'^Dječija_oprema/(?P<d_oprema_id>[0-9]+)/$', views.dd_oprema, name='dd_oprema'),
]