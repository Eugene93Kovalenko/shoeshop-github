from django.test import TestCase

# {
#   "after_expiration": null,
#   "allow_promotion_codes": null,
#   "amount_subtotal": 25000,
#   "amount_total": 25000,
#   "automatic_tax": {
#     "enabled": false,
#     "status": null
#   },
#   "billing_address_collection": null,
#   "cancel_url": "http://127.0.0.1:8000/cancel/",
#   "client_reference_id": null,
#   "consent": null,
#   "consent_collection": null,
#   "created": 1697110830,
#   "currency": "usd",
#   "currency_conversion": null,
#   "custom_fields": [],
#   "custom_text": {
#     "shipping_address": null,
#     "submit": null,
#     "terms_of_service_acceptance": null
#   },
#   "customer": null,
#   "customer_creation": "if_required",
#   "customer_details": {
#     "address": {
#       "city": null,
#       "country": "RU",
#       "line1": null,
#       "line2": null,
#       "postal_code": null,
#       "state": null
#     },
#     "email": "c@yandex.ru",
#     "name": "Eugen Kovalenk",
#     "phone": null,
#     "tax_exempt": "none",
#     "tax_ids": []
#   },
#   "customer_email": null,
#   "expires_at": 1697197230,
#   "id": "cs_test_a1Rxd6JTtLGiz7pNW8PuGpSZd2JHibV5gF8nBhz0Jj1LIKnfZZeLAxlnEv",
#   "invoice": null,
#   "invoice_creation": {
#     "enabled": false,
#     "invoice_data": {
#       "account_tax_ids": null,
#       "custom_fields": null,
#       "description": null,
#       "footer": null,
#       "metadata": {},
#       "rendering_options": null
#     }
#   },
#   "livemode": false,
#   "locale": null,
#   "metadata": {
#     "30": "1"
#   },
#   "mode": "payment",
#   "object": "checkout.session",
#   "payment_intent": "pi_3O0NGPEHgFzglP9y0J6NZyFD",
#   "payment_link": null,
#   "payment_method_collection": "if_required",
#   "payment_method_configuration_details": null,
#   "payment_method_options": {},
#   "payment_method_types": [
#     "card"
#   ],
#   "payment_status": "paid",
#   "phone_number_collection": {
#     "enabled": false
#   },
#   "recovered_from": null,
#   "setup_intent": null,
#   "shipping_address_collection": null,
#   "shipping_cost": null,
#   "shipping_details": null,
#   "shipping_options": [],
#   "status": "complete",
#   "submit_type": null,
#   "subscription": null,
#   "success_url": "http://127.0.0.1:8000/success/",
#   "total_details": {
#     "amount_discount": 0,
#     "amount_shipping": 0,
#     "amount_tax": 0
#   },
#   "url": null
# }



a = {
  "after_expiration": 'null',
  "allow_promotion_codes": 'null',
  "amount_subtotal": 25000,
  "amount_total": 25000,
  "automatic_tax": {
    "enabled": 'false',
    "status": 'null'
  },
  "billing_address_collection": 'null',
  "cancel_url": "http://127.0.0.1:8000/cancel/",
  "client_reference_id": 'null',
  "consent": 'null',
  "consent_collection": 'null',
  "created": 1697111322,
  "currency": "usd",
  "currency_conversion": 'null',
  "custom_fields": [],
  "custom_text": {
    "shipping_address": 'null',
    "submit": 'null',
    "terms_of_service_acceptance": 'null'
  },
  "customer": 'null',
  "customer_creation": "if_required",
  "customer_details": {
    "address": {
      "city": 'null',
      "country": "RU",
      "line1": 'null',
      "line2": 'null',
      "postal_code": 'null',
      "state": 'null'
    },
    "email": "ad@yandex.ru",
    "name": "Eugene Kovalenko",
    "phone": 'null',
    "tax_exempt": "none",
    "tax_ids": []
  },
  "customer_email": "ad@yandex.ru",
  "expires_at": 1697197722,
  "id": "cs_test_a1BiGohkwt91A3vqxncAR6NlZg7jB5q1uZttCQIN56Rlr3z5RUzM0wBXm8",
  "invoice": 'null',
  "invoice_creation": {
    "enabled": 'false',
    "invoice_data": {
      "account_tax_ids": 'null',
      "custom_fields": 'null',
      "description": 'null',
      "footer": 'null',
      "metadata": {},
      "rendering_options": 'null'
    }
  },
  "line_items": {
    "data": [
      {
        "amount_discount": 0,
        "amount_subtotal": 25000,
        "amount_tax": 0,
        "amount_total": 25000,
        "currency": "usd",
        "description": "GREEN BOOTS",
        "id": "li_1O0NNeEHgFzglP9yYDavQApK",
        "object": "item",
        "price": {
          "active": 'false',
          "billing_scheme": "per_unit",
          "created": 1697111322,
          "currency": "usd",
          "custom_unit_amount": 'null',
          "id": "price_1O0NNeEHgFzglP9yEYi8I060",
          "livemode": 'false',
          "lookup_key": 'null',
          "metadata": {},
          "nickname": 'null',
          "object": "price",
          "product": "prod_OmbYcYP8w8eLUa",
          "recurring": 'null',
          "tax_behavior": "unspecified",
          "tiers_mode": 'null',
          "transform_quantity": 'null',
          "type": "one_time",
          "unit_amount": 25000,
          "unit_amount_decimal": "25000"
        },
        "quantity": 1
      }
    ],
    "has_more": 'false',
    "object": "list",
    "url": "/v1/checkout/sessions/cs_test_a1BiGohkwt91A3vqxncAR6NlZg7jB5q1uZttCQIN56Rlr3z5RUzM0wBXm8/line_items"
  },
  "livemode": 'false',
  "locale": 'null',
  "metadata": {
    "30": "1"
  },
  "mode": "payment",
  "object": "checkout.session",
  "payment_intent": "pi_3O0NO1EHgFzglP9y1JMM0eQo",
  "payment_link": 'null',
  "payment_method_collection": "if_required",
  "payment_method_configuration_details": 'null',
  "payment_method_options": {},
  "payment_method_types": [
    "card"
  ],
  "payment_status": "paid",
  "phone_number_collection": {
    "enabled": 'false'
  },
  "recovered_from": 'null',
  "setup_intent": 'null',
  "shipping_address_collection": 'null',
  "shipping_cost": 'null',
  "shipping_details": 'null',
  "shipping_options": [],
  "status": "complete",
  "submit_type": 'null',
  "subscription": 'null',
  "success_url": "http://127.0.0.1:8000/success/",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": 'null'
}

# metadata = {'user': self.request.user}
# for item in cart:
#   metadata['product_info'][item['product_variation'].id] = item['quantity']


SESSION1 = {



  "recovered_from": null,
  "setup_intent": null,
  "shipping_address_collection": null,
  "shipping_cost": null,
  "shipping_details": null,
  "shipping_options": [],
  "status": "complete",
  "submit_type": null,
  "subscription": null,
  "success_url": "http://127.0.0.1:8000/success/",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": null
}


