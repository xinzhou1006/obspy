"""
obspy.io.knet - K-NET and KiK-net ASCII format support for ObsPy
================================================================

This module provides read support for the ASCII format for waveforms from the
K-NET and KiK-net strong-motion seismograph networks operated by the National
Research Institute for Earth Science and Disaster Prevention in Japan
(NIED; http://www.kyoshin.bosai.go.jp/).

KiK-net stations consist of one borehole and one surface sensor which are
distinguished by their channel names:

    ============ ============= ======================
    Channel name  Sensor type   Sensor orientation
    ============ ============= ======================
       NS1        Borehole          N
       EW1        Borehole          E
       UD1        Borehole          Z
       NS2        Surface           N
       EW2        Surface           E
       UD2        Surface           Z
    ============ ============= ======================

K-NET stations only have one surface sensor with the following channel naming
conventions:

    ============ ======================
    Channel name  Sensor orientation
    ============ ======================
       NS            N
       EW            E
       UD            Z
    ============ ======================

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)

Example
-------

Reading K-NET/KiK-net files is handled by using ObsPy's
standard :func:`~obspy.core.stream.read` function. The format is detected
automatically.

>>> from obspy import read
>>> st = read('/path/to/test.knet')
>>> print(st) # doctest: +ELLIPSIS
1 Trace(s) in Stream:
BO.AKT013..EW | 1996-08-10T18:12:24.000000Z - 1996-08-10T18:13:22.990000Z | 100.0 Hz, 5900 samples

Note that K-NET/KiK-net station names are 6 characters long. This will cause
problems if you want to write MiniSEED as it only allows 5 character station
names. In this case you can opt to write the last 2 characters of the station
name into the location field. This is possible because the location is encoded
in the channel name (s.o.).

>>> st = read('/path/to/test.knet',convert_stnm=True)
>>> print(st) # doctest: +ELLIPSIS
1 Trace(s) in Stream:
BO.AKT0.13.EW | 1996-08-10T18:12:24.000000Z - 1996-08-10T18:13:22.990000Z | 100.0 Hz, 5900 samples

Additional header entries from are written to an additional dictionary called
'knet':

>>> print(st[0].stats) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
         network: BO
         station: AKT0
        location: 13
         channel: EW
       starttime: 1996-08-10T18:12:24.000000Z
         endtime: 1996-08-10T18:13:22.990000Z
   sampling_rate: 100.0
           delta: 0.01
            npts: 5900
           calib: 2.38418579102e-06
         _format: KNET
            knet: AttribDict({u'comment': u'A dummy comment', u'stla': 39.6069,
            u'stlo': 140.3213, u'stel': 34.0,
            u'last correction': UTCDateTime(1996, 8, 10, 18, 0),
            u'evla': 38.92, u'mag': 5.9, u'accmax': 4.383, u'duration': 59.0,
            u'evdp': 7.0, u'evot': UTCDateTime(1996, 8, 10, 18, 12),
            u'evlo': 140.63})

The meaning of the entries in the 'knet' dictionary is as follows:
    ==================== ==================================================
       Name                Description
    ==================== ==================================================
       evot               Event origin time (UTC)
       evla               Event latitude
       evlo               Event longitude
       evdp               Event depth
       mag                Event magnitude
       stla               Station latitude
       stlo               Station longitude
       stel               Station elevation
       accmax             Maximum acceleration (after baseline removal)
       duration           Recording duration time [s]
       comment            Comment
       last correction    Time of last correction (Japanese standard time)
    ==================== ==================================================


"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA


if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
