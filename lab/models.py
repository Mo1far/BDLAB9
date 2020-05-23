from django.db import models


class Dept(models.Model):

    deptno = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)

    def __str__(self):
        return self.dname


class Emp(models.Model):

    empno = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=9)
    mgr = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    hiredate = models.DateField()
    sal = models.FloatField(null=True, blank=True)
    comm = models.FloatField(null=True, blank=True)
    deptno = models.ForeignKey(Dept, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.ename
