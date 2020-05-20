from django.shortcuts import render, get_object_or_404
from .models import M_odjeca, M_obuca, M_oprema, Z_oprema, Z_obuca, Z_odjeca, D_oprema, D_obuca, D_odjeca

def pocetna(request):
    return render(request,'pocetna/pocetna.html')

def asortiman(request):
    return render(request,'asortiman/asortiman.html')

def kako(request):
    return render(request,'kako do nas/kako_do_nas.html')

def muskarci(request):
    return render(request,'muski as/muski_as.html')

def zene(request):
    return render(request,'zenski as/zenski_as.html')

def djeca(request):
    return render(request,'djeciji as/djeciji_as.html')

def m_odjeca(request):
    mOdjeca = M_odjeca.objects.all()
    return render(request,'muska odjeca/m_odjeca.html', {'mOdjeca' : mOdjeca})

def m_obuca(request):
    mObuca = M_obuca.objects.all()
    return render(request,'muska obuca/m_obuca.html', {'mObuca' : mObuca})

def m_oprema(request):
    mOprema = M_oprema.objects.all()
    return render(request,'muska oprema/m_oprema.html', {'mOprema' : mOprema})

def z_odjeca(request):
    zOdjeca = Z_odjeca.objects.all()
    return render(request,'zenska odjeca/z_odjeca.html', {'zOdjeca' : zOdjeca})

def z_obuca(request):
    zObuca = Z_obuca.objects.all()
    return render(request,'zenska obuca/z_obuca.html', {'zObuca' : zObuca})

def z_oprema(request):
    zOprema = Z_oprema.objects.all()
    return render(request,'zenska oprema/z_oprema.html', {'zOprema' : zOprema})

def d_odjeca(request):
    dOdjeca = D_odjeca.objects.all()
    return render(request,'djecija odjeca/d_odjeca.html', {'dOdjeca' : dOdjeca})

def d_obuca(request):
    dObuca = D_obuca.objects.all()
    return render(request,'djecija obuca/d_obuca.html', {'dObuca' : dObuca})

def d_oprema(request):
    dOprema = D_oprema.objects.all()
    return render(request,'djecija oprema/d_oprema.html', {'dOprema' : dOprema})

def md_odjeca(request, m_odjeca_id):
     mdOdjeca= get_object_or_404(M_odjeca, pk=m_odjeca_id)
     return render(request, 'muska odjeca/md_odjeca.html', {'mdOdjeca': mdOdjeca })

def md_obuca(request, m_obuca_id):
    mdObuca = get_object_or_404(M_obuca, pk=m_obuca_id)
    return render(request, 'muska obuca/md_obuca.html', {'mdObuca': mdObuca})

def md_oprema(request, m_oprema_id):
    mdOprema = get_object_or_404(M_oprema, pk=m_oprema_id)
    return render(request, 'muska oprema/md_oprema.html', {'mdOprema': mdOprema})

def zd_odjeca(request, z_odjeca_id):
    zdOdjeca = get_object_or_404(Z_odjeca, pk=z_odjeca_id)
    return render(request, 'zenska odjeca/zd_odjeca.html', {'zdOdjeca': zdOdjeca})

def zd_obuca(request, z_obuca_id):
    zdObuca = get_object_or_404(Z_obuca, pk=z_obuca_id)
    return render(request, 'zenska obuca/zd_obuca.html', {'zdObuca': zdObuca})

def zd_oprema(request, z_oprema_id):
    zdOprema = get_object_or_404(Z_oprema, pk=z_oprema_id)
    return render(request, 'zenska oprema/zd_oprema.html', {'zdOprema': zdOprema})

def dd_odjeca(request, d_odjeca_id):
    ddOdjeca = get_object_or_404(D_odjeca, pk=d_odjeca_id)
    return render(request, 'djecija odjeca/dd_odjeca.html', {'ddOdjeca': ddOdjeca})

def dd_obuca(request, d_obuca_id):
    ddObuca = get_object_or_404(D_obuca, pk=d_obuca_id)
    return render(request, 'djecija obuca/dd_obuca.html', {'ddObuca': ddObuca})

def dd_oprema(request, d_oprema_id):
    ddOprema = get_object_or_404(D_oprema, pk=d_oprema_id)
    return render(request, 'djecija oprema/dd_oprema.html', {'ddOprema': ddOprema})

