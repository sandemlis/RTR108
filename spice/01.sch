v 20130925 2
C 40000 40000 0 0 0 title-B.sym
N 44200 46500 44200 47000 4
N 44200 47000 45000 47000 4
N 45900 47000 46500 47000 4
N 46500 47000 46500 46600 4
N 46500 45700 46500 45300 4
N 44200 45300 46500 45300 4
N 44200 45300 44200 45600 4
{
T 44200 45300 5 10 0 0 0 0 1
netname=0
}
C 44000 46500 1 270 0 voltage-3.sym
{
T 44700 46300 5 8 0 0 270 0 1
device=VOLTAGE_SOURCE
T 44500 46200 5 10 1 1 270 0 1
refdes=V1
T 43800 46200 5 10 1 1 270 0 1
value=13.6
}
C 45000 46900 1 0 0 resistor-2.sym
{
T 45400 47250 5 10 0 0 0 0 1
device=RESISTOR
T 45300 47200 5 10 1 1 0 0 1
refdes=R1
T 45400 46700 5 10 1 1 0 0 1
value=4
}
C 46400 46600 1 270 0 resistor-2.sym
{
T 46750 46200 5 10 0 0 270 0 1
device=RESISTOR
T 46700 46300 5 10 1 1 270 0 1
refdes=R2
T 46200 46200 5 10 1 1 270 0 1
value=7
}
