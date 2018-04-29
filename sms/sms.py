from Hologram.HologramCloud import HologramCloud

toNumber="+6590692841"
message='{"V":"5","I":"1}'

hologram = HologramCloud(dict(), network='cellular')
hologram.network.modem.set("CMGW", toNumber)
hologram.network.modem.serial_port.write(message)