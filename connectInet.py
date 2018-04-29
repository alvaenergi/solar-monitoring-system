try:
    from Hologram.HologramCloud import HologramCloud

    # Create Hologram class network object
    hologram = HologramCloud(dict(), network='cellular')
    # Connect to the Hologram Global Network
    result = hologram.network.connect()
except:
    print("Hologram network error")