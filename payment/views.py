import json
import requests
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10
    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    zarinpal_url = 'https://gateway.zibal.ir/v1/request'
    # zarinpal_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'
    request_data_payment = {
        # 'merchant': settings.ZARINPAL_MERCHANT_ID,
        'merchant': 'zibal',
        # 'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        # 'MerchantID': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        # 'Amount': rial_total_price,
        'description': f'#{order.id}:{order.user.first_name} {order.user.last_name}',
        # 'Description': f'#{order.id}:{order.user.first_name} {order.user.last_name}',
        'callbackUrl': request.build_absolute_uri(reverse('payment:payment_callback'))
        # 'callbackUrl': 'http://127.0.0.1:8000',
        # 'callback_url': 'http://127.0.0.1:8000'
        # 'CallbackURL': 'http://127.0.0.1:8000'
    }
    res = requests.post(url=zarinpal_url, data=json.dumps(request_data_payment), headers=request_header)
    print(res.json())
    data = res.json()
    # data = res.json()['data']
    trackId = data['trackId']
    # authority = data['authority']
    order.zibal_trackId = trackId
    order.save()
    # if len(res.json()['errors']) == 0:

    if data['message'] == 'success':
        # return redirect(f'https://www.zarinpal.com/pg/startpay/{authority}')
        # return redirect('https://www.zarinpal.com/pg/startpay/{authority}'.format(authority=authority))

        return redirect('https://gateway.zibal.ir/start/{trackId}'.format(trackId=trackId))

    else:
        return HttpResponse('Error From ZarinPal')


def payment_callback(request):
    payment_success = request.GET.get('success')
    payment_status = request.GET.get('status')
    payment_trackId = request.GET.get('trackId')
    order = get_object_or_404(Order, zibal_trackId=payment_trackId)
    order_id = order.id
    # print(f'ORDER ID:{order_id}')
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == '2':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }

        request_payment_data = {
            'merchant': 'zibal',
            'amount': rial_total_price,
            'trackId': payment_trackId,
            # 'orderId': order_id,
            # 'description': 'TARAKONESH--->>MOVAFAGH',

        }

        res = requests.post(
            url='https://gateway.zibal.ir/v1/verify',
            data=json.dumps(request_payment_data),
            headers=request_header,

        )

        data = res.json()
        print(f'DATA IS :{data}')
        if (data['message'] == 'success') and (data['result'] == 100):
            payment_result = data['result']
            if payment_result == 100:
                order.is_paid = True
                # order.zibal_refNumber = data['refNumber']
                order.zibal_data = data
                order.save()
                return HttpResponse('پرداخت شماباموفقیت انجام شد')

            elif payment_result == 201:
                return HttpResponse('پرداخت شماباموفقیت انجام شد البته این تراکنش قبلا تایید شده است ')
            # else:
            #     return HttpResponse('پرداخت شماباموفقیت انجام شد البته این تراکنش قبلا تایید شده است ')

    else:

        return HttpResponse('پرداخت ناموفق')
