from django.shortcuts import render
from django.http import HttpResponse
from .modules import test_scrape_web as noisy
from signup.models import Profile, Product

def index(request):
    '''if request.method == 'POST':'''
            #output = [[1, 2, 3, 4, 5]]
    price_range = [int(request.POST['min_price']), int(request.POST['max_price'])]
    output = noisy.main(request.POST['search'], price_range)
    
    #product is being stored in the session
    #request.user.profile.temp_result_dict['results'] = output['data_list']
    request.session['temp_results'] = output['data_list']
    #print(output['product_list'])
    
    return render(request, 'results/home.html', {"list": output['product_list']})
            #return render(request, 'home/home.html', {'list': output})


def search(request):
    output = noisy.main(request.POST['search'])
    return render(request, 'results/home.html', {"list": output})

    #return HttpResponse(arg)
    '''response = HttpResponse(alarm, content_type='text/plain')
    response_a = do_something(response)
    return response_a'''

'''def post(request):
    form = HomeForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']
        args = {'form': form, 'text': text}
        return render(request, 'home/home.html', args)'''

def post(request, text):
    print('request.POST')

def YOUR_VIEW(request, pk):
    YOUR_OBJECT.objects.filter(pk=pk).update(views=F('views')+1)
    return HttpResponseRedirect(request.GET.get('next'))

