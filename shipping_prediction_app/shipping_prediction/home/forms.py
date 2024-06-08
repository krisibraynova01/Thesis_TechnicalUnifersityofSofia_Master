from django import forms

class ShippingPredictionForm(forms.Form):
    days_for_shipment_scheduled = forms.FloatField(label='Days for Shipment (Scheduled)')
    delivery_status = forms.ChoiceField(choices=[('Advance shipping', 'Advance shipping'), ('Late delivery', 'Late delivery'), ('Shipping canceled', 'Shipping canceled'), ('Shipping on time', 'Shipping on time')], label='Delivery Status')
    shipping_mode = forms.ChoiceField(choices=[('Regular Air', 'Regular Air'), ('Express Air', 'Express Air'), ('Ship', 'Ship')], label='Shipping Mode')
    order_region = forms.CharField(label='Order Region')
    order_state = forms.CharField(label='Order State')
    order_city = forms.CharField(label='Order City')
    order_country = forms.CharField(label='Order Country')
    customer_city = forms.CharField(label='Customer City')
    customer_country = forms.CharField(label='Customer Country')
    order_year = forms.IntegerField(label='Order Year')
    order_month = forms.IntegerField(label='Order Month')