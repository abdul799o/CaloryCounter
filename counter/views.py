from django.shortcuts import render

# Create views here.

#szkLSqDuh0ntXU6DAZoieg==7SjaxRlvTfwKIFxB

#{}'.format(query)

def home(request):
    import json
    import requests
    if request.method == "POST":
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url  + query, headers = {'X-Api-Key': 'szkLSqDuh0ntXU6DAZoieg==7SjaxRlvTfwKIFxB'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Whoops, an error occured"
            print(e)
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html' ,{'query':'Enter a valid input'})


#     response = requests.get(api_url, headers={'X-Api-Key': 'szkLSqDuh0ntXU6DAZoieg==7SjaxRlvTfwKIFxB'})
#     if response.status_code == requests.codes.ok:
#         print(response.text)
#     else:
#         print("Error:", response.status_code, response.text)


#return render(request, 'home.html')
