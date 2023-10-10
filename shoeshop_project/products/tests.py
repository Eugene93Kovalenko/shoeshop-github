from django.test import TestCase


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
  "created": 1696868922,
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
  "expires_at": 1696955322,
  "id": "cs_test_a1oKXI4bfF2fBnIilVjaC4EaZ3NYeYvPtkvPncWjVsh1fO3KNtXN6azemW",
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
  "livemode": 'false',
  "locale": 'null',
  # "metadata":  {
  #   "30": "GREEN BOOTS / 47 size",
  #   "quantity": "1"
  # },

  "mode": "payment",
  "object": "checkout.session",
  "payment_intent": "pi_3NzMKAEHgFzglP9y0ShPy3GM",
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




# {\n  "id": "evt_3Nzee0EHgFzglP9y1tVxQAiV",\n  "object": "event",\n  "api_version": "2023-08-16",\n  "created": 1696939358,\n  "data": {\n    "object": {\n      "id": "pi_3Nzee0EHgFzglP9y15GE8YBW",\n      "object": "payment_intent"
# ,\n      "amount": 38000,\n      "amount_capturable": 0,\n      "amount_details": {\n        "tip": {\n        }\n      },\n      "amount_received": 38000,\n      "application": null,\n      "application_fee_amount": null,\n      "a
# utomatic_payment_methods": null,\n      "canceled_at": null,\n      "cancellation_reason": null,\n      "capture_method": "automatic",\n      "client_secret": "pi_3Nzee0EHgFzglP9y15GE8YBW_secret_jSWK1Nx8Ht07uZFDDeIRHpAyE",\n      "c
# onfirmation_method": "automatic",\n      "created": 1696939356,\n      "currency": "usd",\n      "customer": null,\n      "description": null,\n      "invoice": null,\n      "last_payment_error": null,\n      "latest_charge": "ch_3N
# zee0EHgFzglP9y1yCY4PmD",\n      "livemode": false,\n      "metadata": {\n      },\n      "next_action": null,\n      "on_behalf_of": null,\n      "payment_method": "pm_1Nzee0EHgFzglP9y3fHgfCUx",\n      "payment_method_configuration_
# details": null,\n      "payment_method_options": {\n        "card": {\n          "installments": null,\n          "mandate_options": null,\n          "network": null,\n          "request_three_d_secure": "automatic"\n        }\n
#   },\n      "payment_method_types": [\n        "card"\n      ],\n      "processing": null,\n      "receipt_email": null,\n      "review": null,\n      "setup_future_usage": null,\n      "shipping": null,\n      "source": null,\n
#   "statement_descriptor": null,\n      "statement_descriptor_suffix": null,\n      "status": "succeeded",\n      "transfer_data": null,\n      "transfer_group": null\n    }\n  },\n  "livemode": false,\n  "pending_webhooks": 2,\n  "r
# equest": {\n    "id": "req_vNb5yS3XWWuTT0",\n    "idempotency_key": "20502fbc-f957-4784-a4e9-533da119e601"\n  },\n  "type": "payment_intent.succeeded"\n}'
#
#
#
# {\n  "id": "evt_3Nzee0EHgFzglP9y1VbGeE2L",\n  "object": "event",\n  "api_version": "2023-08-16",\n  "created": 1696939356,\n  "data": {\n    "object": {\n      "id": "pi_3Nzee0EHgFzglP9y15GE8YBW",\n      "object": "payment_intent"
# ,\n      "amount": 38000,\n      "amount_capturable": 0,\n      "amount_details": {\n        "tip": {\n        }\n      },\n      "amount_received": 0,\n      "application": null,\n      "application_fee_amount": null,\n      "autom
# atic_payment_methods": null,\n      "canceled_at": null,\n      "cancellation_reason": null,\n      "capture_method": "automatic",\n      "client_secret": "pi_3Nzee0EHgFzglP9y15GE8YBW_secret_jSWK1Nx8Ht07uZFDDeIRHpAyE",\n      "confi
# rmation_method": "automatic",\n      "created": 1696939356,\n      "currency": "usd",\n      "customer": null,\n      "description": null,\n      "invoice": null,\n      "last_payment_error": null,\n      "latest_charge": null,\n
#    "livemode": false,\n      "metadata": {\n      },\n      "next_action": null,\n      "on_behalf_of": null,\n      "payment_method": null,\n      "payment_method_configuration_details": null,\n      "payment_method_options": {\n
#       "card": {\n          "installments": null,\n          "mandate_options": null,\n          "network": null,\n          "request_three_d_secure": "automatic"\n        }\n      },\n      "payment_method_types": [\n        "card"\
# n      ],\n      "processing": null,\n      "receipt_email": null,\n      "review": null,\n      "setup_future_usage": null,\n      "shipping": null,\n      "source": null,\n      "statement_descriptor": null,\n      "statement_desc
# riptor_suffix": null,\n      "status": "requires_payment_method",\n      "transfer_data": null,\n      "transfer_group": null\n    }\n  },\n  "livemode": false,\n  "pending_webhooks": 2,\n  "request": {\n    "id": "req_vNb5yS3XWWuTT
# 0",\n    "idempotency_key": "20502fbc-f957-4784-a4e9-533da119e601"\n  },\n  "type": "payment_intent.created"\n}


