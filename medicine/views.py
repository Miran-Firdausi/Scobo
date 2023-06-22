from django.shortcuts import render
import paho.mqtt.client as mqtt


def publish_message(topic, message):
    client = mqtt.Client("P16885868")
    client.connect("mqtt.eclipseprojects.io")
    client.publish(topic, message)
    print("Published sucessssss")


def pill_dispenser(request):
    if request.method == "POST":
        medicine = request.POST.get("medicine")
        # mqtt_publish.single("scobo", payload=medicine, hostname="mqtt://broker.emqx.io")
        publish_message("scobo/medicine", str(medicine))
        return render(request, 'pill-dispenser.html', {'dispenser_page': True, 'medicine': medicine})
    return render(request, 'pill-dispenser.html', {'dispenser_page': True})


def about(request):
    return render(request, 'about.html', {'about_page': True})
