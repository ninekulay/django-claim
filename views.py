from django.shortcuts import render,redirect
from .models import ClaimPage
from django.contrib.auth.models import User
import datetime

def NewClaim(request): 
	if request.method == 'POST' :
		username = request.user.username
		user = User.objects.get(username=username)
		data = request.POST.copy()
		Stamp = datetime.datetime.now().strftime('%Y%m%d')
		BrandType = data.get('BrandType')
		ModelType = data.get('ModelType')
		SlType = data.get('SlType')
		Deliverydate = data.get('Deliverydate')
		MdSerial  =data.get('MdSerial')
		DetailDamage = data.get('DetailDamage')
		
		x = 1
		x = str(x).zfill(3)
		dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')		
		Claimid = 'Claim' + username + dt[2:4] + dt[4:6] + '-' + x
		while ClaimPage.objects.filter(Claimid=Claimid).exists():
			x = int(x)
			x = x+1
			x = str(x).zfill(3)
			Claimid = 'TPR' + username + dt[2:4] + dt[4:6] + '-' + x

		new = ClaimPage()
		try:
			if not Deliverydate:
				Deliverydate = None
			else :
				new.Deliverydate = Deliverydate
		except :
			pass	
		try:			
			file_image = request.FILES['Photouser1']
			file_image_name = request.FILES['Photouser1'].name.replace(' ','')
			res2 = ""
			i = random.randint(1, 9)
			i = str(i)
			res2 = res2 + i
			res = [idx for idx in file_image_name if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]		
			for i in res:
				res2 = res2 + i					
			fs = FileSystemStorage()
			filename = fs.save(res2,file_image)
			upload_file_url = fs.url(res2)
			new.Photouser1 = upload_file_url[6:]
		except:
			pass
		new.BrandType = BrandType
		new.ModelType = ModelType
		new.Stamp = Stamp
		new.SlType = SlType
		new.MdSerial  = MdSerial
		new.DetailDamage = DetailDamage
		new.Claimid = Claimid
		new.user = user
		new.save()
	return render(request, 'myapp/newclaim.html')

def ClaimList(request):
	username = request.user.username
	user = User.objects.get(username=username)
	context = {}
	claimlist = ClaimPage.objects.filter(user=user).order_by('id').reverse()		
	context['claimlist'] = claimlist
	return render(request,'myapp/orderlist.html',context)
