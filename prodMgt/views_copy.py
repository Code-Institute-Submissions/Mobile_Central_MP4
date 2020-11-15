from django.shortcuts import render
from .forms import AddProductForm, AddBrandForm, AddSideForm, ProdList, EditProductForm
from products.models import Product, Category, CaroPics
from home.views import get_referer_view

# We're in prodMgt views.

def AddProduct(request):
    pName=""
    AddProd=()
    bName=""
    AddBrand=()
    AddSidePic=()
    EditProd=()
    cProduct=""
    eName=""
    pForm = AddProductForm() 
    bForm = AddBrandForm()
    cForm = AddSideForm()
    eForm= EditProductForm()
    lookupProd = ProdList()
    dpForm=()
    caropics=()
    selSideProd=""
    sidePicDeletion=""
    pic_to_del=""
    subForm=""
    TheSidePic=""
    Dear=""
    selprodId=""
    pDeleted=""
    theresPic=""
    p_to_change=""
    pChanged = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear= str(request.user.first_name)
    if request.method == 'POST':
        print(request.POST)
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']
        if 'pic_to_del' in request.POST:
            pic_to_del = request.POST['pic_to_del']

        print('quale is: ', subForm)
        print('pic_to_del is: ', pic_to_del)
        if subForm == 'prod':
            
            try:
                pForm = AddProductForm(request.POST, request.FILES)
                
                if pForm.is_valid():
                    pForm.save()
                    # name = request.POST['name']
                    AddProd=pForm.instance
                    pName=AddProd.name

            except:
                pForm = AddProductForm() 

        elif  subForm == 'sidepic':   
            try:    
                cForm = AddSideForm(request.POST, request.FILES)

                if cForm.is_valid():
                    cForm.save()
                    AddSidePic=cForm.instance
                    # bName = request.POST['name']
                    cProduct = AddSidePic.product
            except:
                cForm = AddSideForm()

        elif  subForm == 'brand':   
            try:    
                bForm = AddBrandForm(request.POST)

                if bForm.is_valid():
                    bForm.save()
                    AddBrand=bForm.instance
                    # bName = request.POST['name']
                    bName = AddBrand.name
            except:
                bForm = AddBrandForm()

        elif subForm == 'findProd':
            theProd = request.POST['lookupProd']
            # print('theProd is: ', theProd)
            selProd=Product.objects.get(id=theProd)
            print(selProd)
            EditProd=EditProductForm(instance=selProd)
            # print(EditProd)
            eForm=EditProd
            selprodId=theProd

        elif subForm == 'editProd':

            try:
                eForm=EditProductForm(request.POST, request.FILES)
                if 'with_prod_id' in request.POST:
                    with_prod_id = request.POST['with_prod_id']
                    pickprod= Product.objects.get(id=with_prod_id)
                else:
                    theProd = request.POST['name']
                    pickprod= Product.objects.get(name=theProd)

                if 'p_to_del' in request.POST:
                    # print('theProd is: ', theProd)
                    
                    # print (pickprod)
                    print (str(eForm))
                    # print(str(request.POST))
                    print ('Imma delete', pickprod )
                    # if eForm.is_valid():
                        
                    pDeleted=str(pickprod)

                    pickprod.delete()
                    # eForm = EditProductForm(request.POST, request.FILES)
                    # EditProd=EditProductForm(instance=theProd )
                    # if eForm.is_valid():
                    #     EditProd=eForm
                    #     EditProd.save()
                    #     # eForm.save()
                    #     # # name = request.POST['name']
                    #     # EditProd=eForm.instance
                    #     eName=EditProd.name
                    
                elif 'p_to_del' not in request.POST:
                    
                    
                    
                    p_to_change = Product.objects.get(id=pickprod.id)
                    print('p_to change isss: ', p_to_change)
                    eName = str(pickprod)
                    if 'name' in request.POST:

                        p_to_change.name = request.POST['name']
                        pChanged = p_to_change
                    if 'price' in request.POST:    
                        p_to_change.price = request.POST['price']
                        pChanged = p_to_change
                    if 'description' in request.POST:
                        p_to_change.description = request.POST['description']
                        pChanged = p_to_change
                    if 'stock' in request.POST:    
                        p_to_change.stock = request.POST['stock']
                        pChanged = p_to_change
                    if 'available' in request.POST:
                        if 'available' in request.POST:
                            available = request.POST['available']
                            if available == 'on':
                                p_to_change.available = True
                                pChanged = p_to_change
                    else:
                        p_to_change.available = False
                    if 'latest' in request.POST:
                        latest = request.POST['latest']
                        if latest == 'on':
                            p_to_change.latest = True
                            pChanged = p_to_change
                    else:
                        p_to_change.latest = False
                    if 'best' in request.POST:
                        best = request.POST['best']
                        if best == 'on':
                            p_to_change.best = True
                            pChanged = p_to_change
                    else:
                        p_to_change.best = False

                    if 'category' in request.POST:
                        upCategory = request.POST['category']
                        pickCateg = Category.objects.get(id=upCategory)
                        p_to_change.category = pickCateg
                        pChanged = p_to_change

                    if 'image' in request.FILES:
                            upImage = request.FILES['image']
                            p_to_change.image = upImage
                            theresPic = str(p_to_change)
                            print('thersePic', theresPic)
                            pChanged = p_to_change
                    p_to_change.save()

            except Exception as e :
                raise e
                # eForm = EditProductForm()
        
        elif subForm == 'findSideProd':
            theProd = request.POST['lookupProd']
            # print('theProd is: ', theProd)
            selSideProd=Product.objects.get(id=theProd)
            # print(selProd)
            # delSideProd=EditProductForm(instance=selProd)
            # # print(EditProd)
            # eForm=EditProd
            caropics = CaroPics.objects.filter(product=selSideProd)
            print(str(caropics))

        if pic_to_del :
            print('ok del side pic lo sente')
            

            # SidePicId = request.POST['pic_to_del']
            # print(str(SidePicId))
            TheSidePic = CaroPics.objects.get(id=pic_to_del)
            TheSidePic.delete()

            print('il caro Side pic e\': (stu basatru)',str(TheSidePic))
            sidePicDeletion="deleted"

            
            


    else:
        pForm = AddProductForm()
        bForm = AddBrandForm()
        cForm = AddSideForm()
        eForm = AddProductForm() 
        dpForm=()

    this_url = request.path
    referer_view = get_referer_view(request)

    context={
        'pForm':pForm,
        'pName':pName,
        'AddProd':AddProd,
        'AddBrand':AddBrand,
        'AddSidePic':AddSidePic,
        'bForm':bForm,
        'bName':bName,
        'cProduct':cProduct,
        'cForm':cForm,
        'eForm':eForm,
        'EditProd':EditProd,
        'eName':eName,
        'lookupProd':lookupProd,
        'caropics':caropics,
        'selSideProd':selSideProd,
        'sidePicDeletion':sidePicDeletion,
        'dpForm':dpForm,
        'TheSidePic':TheSidePic,
        'Dear':Dear,
        'selprodId':selprodId,
        'this_url':this_url,
        'referer_view':referer_view,
        'pDeleted':pDeleted,
        'theresPic':theresPic,
        'p_to_change':p_to_change,
        'pChanged': pChanged,

    }
    return render (request,'addProduct.html',context)