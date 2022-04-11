'''
Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

Employee should have the following attributes:
StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,

For Example:

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)

Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)

We will assume a standard rate of 20% and a higher rate of 40%, and that PRSI at 4% is not subject to allowances. (we will ignore USC etc.)

>>>jg.computePayment(42, '31/10/2021')

{'name': 'Joe Green', 'Date':'31/10/2021', 'Regular Hours Worked':37,'Overtime Hours Worked':5,'Regular Rate':16,'Overtime Rate':24, 'Regular Pay':592,'Overtime Pay':120,'Gross Pay':712, 'Standard Rate Pay':710,'Higher Rate Pay':2, 'Standard Tax':142,'Higher Tax':0.8,'Total Tax':142.8,'Tax Credit':72, 'Net Tax':70.8, 'PRSI': 28.48,'Net Deductions':99.28, 'Net Pay': 612.72}

Test your class and method thoroughly, and at a minimum include test cases testing the following:

Net pay cannot exceed gross pay 

#TestMethod

def testNetLessEqualGross(self):
  e=Employee(#Joe Green's Information)
  pi=e.computePayment(1,'31/10/2021')
  self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

Overtime pay or overtime hours cannot be negative.

Regular Hours Worked cannot exceed hours worked

Higher Tax cannot be negative.

Net Pay cannot be negative.
'''

import unittest
#created class Employee with the following attributes
class Employee:
    def __init__(self, staff_id, last_name, first_name, regHours, hourlyRate, otMultiple, taxCredit, standardBand) :
        self.__staffID = staff_id
        self.__lastName = last_name
        self.__firstName = first_name
        self.__regHours = regHours
        self.__hourlyRate = hourlyRate
        self.__otMultiple = otMultiple
        self.__taxCredit = taxCredit
        self.__standardBand = standardBand

    #Created a method computePayment which takes HoursWorked and date as input, and returns a payment information
    def computePayment(self, hoursWorked, date):
        if(hoursWorked < 0):
            raise ValueError("Hours worked Cannot be negative")

        if(self.__regHours >= hoursWorked):
           raise ValueError("Regular Hours Cannot be exceed Hours worked")
        
        reg_hrs_wrked = self.__regHours
        ot_hrs_wrked = 0
        if(hoursWorked >= self.__regHours):    
            ot_hrs_wrked = hoursWorked - self.__regHours
        else:
            reg_hrs_wrked = hoursWorked

        rg_rate = self.__hourlyRate
        ot_rate = self.__hourlyRate * self.__otMultiple
        
        #calculate regular, Overtime and gross pay
        rg_pay = reg_hrs_wrked * rg_rate
        ot_pay = ot_hrs_wrked * ot_rate
        gross_pay = rg_pay * ot_pay
             
        st_rate_pay = self.__standardBand
        if(ot_hrs_wrked == 0):
            higher_rate_pay = 0
        else:
            higher_rate_pay = gross_pay - st_rate_pay
        
        if(higher_rate_pay <= 0):
            higher_rate_pay = 0

        #calculatee standard and higher pay tax
        if(gross_pay <= st_rate_pay):
            st_tax = round(((gross_pay*20)/100),2)
        else:
            st_tax = round(((st_rate_pay*20)/100),2)
        higher_tax = round(((higher_rate_pay*40)/100),2)
        
        #calculate tax
        total_pay = st_tax + higher_tax
        tax_credit = self.__taxCredit
        net_tax = round(total_pay - tax_credit,2)
        prsi = round(((gross_pay*4)/100),2)

        #calculate net deduction and net pay
        net_deductions = round(net_tax + prsi,2)
        net_pay = round(gross_pay - net_deductions,2)
        
        if(net_pay <= 0):
            raise ValueError("Net Pay Cannot be Negative")
        #creating dictionary 
        pay={}
        pay['name'] = self.__firstName+" "+self.__lastName
        pay['Date'] = date
        pay['Regular Hours Worked'] = reg_hrs_wrked
        pay['Overtime Hours Worked'] = ot_hrs_wrked   
        pay['Regular Hours Worked'] = hoursWorked
        pay['Regular Rate'] = rg_rate
        pay['Overtime Rate'] = ot_rate
        pay['Regular Pay'] = rg_pay
        pay['Overtime Pay'] = ot_pay
        pay['Gross Pay'] = gross_pay
        pay['Standard Rate Pay'] = st_rate_pay
        pay['Higher Rate Pay'] = higher_rate_pay
        pay['Standard Tax'] = st_tax
        pay['Higher Tax'] = higher_tax
        pay['Total Tax'] = total_pay
        pay['Tax Credit'] = tax_credit
        pay['Net Tax'] = net_tax
        pay['PRSI'] = prsi
        pay['Net Deductions'] = net_deductions
        pay['Net Pay'] = net_pay
        
        return pay

class Unit_test(unittest.TestCase):
    #NetLessEqualGross
    def testNetLessEqualGross(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.computePayment(47, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])
    #Overtime pay or overtime hours cannot be negative.
    def testOvertimeNegative(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        with self.assertRaises(ValueError):
            e.computePayment(-10,'31/10/2021')
    #Regular Hours Worked cannot exceed hours worked
    def testRegHrLessEqualHrWrked(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        with self.assertRaises(ValueError):
            e.computePayment(30,'31/10/2021')
    #Higher Tax cannot be negative.
    def testHigherTaxNegative(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(38, '31/10/2021')
        self.assertGreaterEqual(pi['Higher Tax'], 0)
    #Net Pay cannot be negative
    def testNetPayNegative(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(48, '31/10/2021')
        self.assertGreaterEqual(pi['Net Pay'], 0)

unittest.main(argv=['ignored'], exit=False)