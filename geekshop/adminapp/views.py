from django.shortcuts import  render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from adminapp.forms import ProductCategoryEditForm, ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
  #  title = 'админка/пользователи'

   # users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

   # content = {
   #     'title': title,
   #     'objects': users_list
   # }

   # return render(request, 'adminapp/users.html', content)

class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка пользователя'

        return context



@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        if user_item.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user_to_delete': user_item
    }

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all('-is_active', '-id')

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


#@user_passes_test(lambda u: u.is_superuser)
#def category_create(request):
   # title = 'категории/создание'

   # if request.method == 'POST':
      #  category_form = ProductCategoryEditForm(request.POST, request.FILES)
       # if category_form.is_valid():
          #  category_form.save()
           # return HttpResponseRedirect(reverse('admin:categories'))
    #else:
       # category_form = ProductCategoryEditForm()
#
  #  content = {'title': title, 'update_form': category_form}

   # return render(request, 'adminapp/category_update.html', content)


#@user_passes_test(lambda u: u.is_superuser)
#def category_update(request, pk):
   # title = 'категории/редактирование'

   # category = get_object_or_404(ProductCategory, pk=pk)
   # if request.method == 'POST':
       # edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        #if edit_form.is_valid():
           # edit_form.save()
          #  return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
   # else:
      #  edit_form = ProductCategoryEditForm(instance=edit_category)

   # content = {'title': title, 'update_form': edit_form}

   # return render(request, 'adminapp/category_update.html', content)

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp/categories.html')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/создание'

        return context

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp/categories.html')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/изменение'

        return context

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp/categories.html')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/изменение'

        return context

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.is_active = False
        object.save()

        return HttpResponseRedirect(self.get_success_url())

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
   title = 'админка/продукт'

   category = get_object_or_404(ProductCategory, pk=pk)
   products_list = Product.objects.filter(category__pk=pk).order_by('name')

   content = {
        'title': title,
        'category': category,
        'objects': products_list
    }
   return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт/создать'
    product = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk] ))
    else:
        product_form = ProductEditForm()
    content = {
        'title': title,
         'update_form': product_form,
         'category': category,
    }
    return render(request, 'adminapp/product_update.html', content)


#@user_passes_test(lambda u: u.is_superuser)
#def product_read(request, pk):
    #title = 'продукт/подробнее'
    #product = get_object_or_404(Product,pk=pk)
    #content = {
        #'title': title,
      #  'objects': products,
  #  }

   # return render(request, 'adminapp/product_read.html', content)

class ProductDetailsView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукт/редактировать'
    edit_form =  get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(requestust.POST, requestust.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[pk] ))
        else:
            edit_form=ProductEditForm(instance=edit_product)
        content = {
            'title': title,
            'update_form': edit_form,
            'category': edit_product.category,
        }

        return render(request, 'adminapp/product_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:product', args=[product.category.pk]))

    content = {
        'title': title,
        'product_to_delete': product,
    }
    return render(request, 'adminapp/product_delete.html', content)