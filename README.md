# CP_device
Cerebral Palsy device and software.

This project is about helping children with compromised muscle
function that affects one of their hands, the recessive hand (RH).
This could be due to any of several factors such as Erb's palsy.

The proposed remedy is to encourage use the RH rather than favor the
dominant hand (DH) so that recovery speeds up.  The idea is to create
a device requiring manipulation by the RH, while occupying the DH in
keeping the device active.

In this case the device has a bush button that is to be continuously
depressed by the DH, while the RH operates the device.  In the
first iteration, we have a push button being monitored by a Raspberry
PI (RP).

When depressed, the RP starts playing music, when released, the RP
pauses the music and restarts the music when subsequently depressed.
This iteration does not engage the RH, but is just a proof of concept.

Next is to implement a game that is played by the RH instead of
playing music. The game pauses if the DH releases the switch and
continues when the DH presses the push button.

Participants.

The idea for this device was envisaged by Virginia Quellmalz-Zallocco
who observered the care given to these children during her health care
studies.

Virginia designed and constructed the enclosure, and is responsible
for marketing the product. Recently presented the need, and
demonstrated the device at Carnegie University as a potential for
research project and accepted as such by senior students.

The coding, circuit design and implementation for the first iteration
was done by Mauro Zallocco.
