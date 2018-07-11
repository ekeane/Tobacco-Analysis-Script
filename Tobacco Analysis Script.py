
# coding: utf-8

# # Tobacco Analysis Program

# In[2]:


from typing import NamedTuple, List
from matplotlib import pyplot
from cs103 import *
import csv


# # Step 1a: Identify the information in the file your program will read
The information I have access to is:

- Year (int)
- State (str)
- Percentage of state population that smoked everyday(float)
- Percentage of state population that smoked some days (float)
- Percentage of state population that was a former smoker (float)
- Percentage of state population that never smoked (float)
- Location 1 (str)
# # Step 1b: Write a description of what your program will produce
Some possible outputs I could produce using the data above are:

- a line graph of smoking everyday vs year for the state of Puerto Rico
- a bar chart showing the difference of the earliest year of smoking everyday data vs the latest year for a particular state
- a line graph of a few states comparing the percentages of never smoked over time 
- a line graph of smoking everyday vs former smoker over years for the state of Puerto Rico

I want to output a line graph with the year on the y axis and Smoke Everday (in percent) and Former Smoker (in percent) on the x axis. This smoking data will be for the state of Puerto Rico, producing a line graph with two lines 
hopefully showing that as time has progressed smoking everday has decreased while former smoker percentage has increased. 
# # Step 1c: Write or draw examples of what your program will produce
                                   
                      25.0   | *-_                
                             |    \*---_             
                      20.0   |         \*---_                                  Descending Line: Smoke Everyday (%)
                             |               \                                 Ascending Line: Former Smoker (%)
 Percentage (%)       15.0   |                \*----_            _*                
                             |                       \_     _*---/            
                      10.0   |                       _*\---/   
                             |              _*------/   \*---_      
                      5.0    |     ___*----/                  \---* 
                             |  __/                         
                             +------------------------------------------------
                               1995      2000       2005       2010  
                    
                                                  Years
# # Step 2a: Design data definitions
# 

# In[3]:


PuertoRicoSmokeData = NamedTuple('PuertoRicoSmokeData', [('year', int), # in range [1996, 2010]
                                                               ('state', str), 
                                                               ('smoke_everyday', float), # in range [0, 100]
                                                               ('former_smoker', float)]) # in range [0, 100]

# interp. a percentage of smoking everday vs former smoker in the state of Puerto Rico with year (int), 
# state (str), a percentage of who smoke everday (float), and former smoker percentage (float)

PRSD1 = PuertoRicoSmokeData(1996, 'Puerto Rico', 9.40, 16.0)
PRSD2 = PuertoRicoSmokeData(1997, 'Puerto Rico', 9.40, 15.70)
PRSD3 = PuertoRicoSmokeData(1998, 'Puerto Rico', 10.10, 16.80)

def fn_for_puerto_rico_smoke_data(prsd: PuertoRicoSmokeData) -> ...: # template based on Compound
    return ...(prsd.year, 
               prsd.state, 
               prsd.smoke_everday,
               prsd.former_smoker)
    
# List[PuertoRicoSmokeData]
# interp. a list of smoking everday and former smoker percentages over the years for the state of Puerto Rico

L0 = []
L1 = [PRSD1, PRSD2]
L2 = [PRSD1, PRSD2, PRSD3]

def fn_for_loprsd(loprsd: List[PuertoRicoSmokeData]) -> ...: # template based on arbitrary-sized
                                                                # and the reference rule
    # description of the acc
    acc = ... # type: ...
    for prsd in loprsd:
        acc = ...(acc, fn_for_puerto_rico_smoke_data(prsd))
    return acc  


# Why this information is crucial for what I will be analyzing:

# This information is crucial because I want to output a line graph with the year on the y axis 
# and Smoke Everday (in percent) and Former Smoker (in percent) on the x axis. Therefore it is crucial
# that I have year, state, smoke everyday and former smoker in my data definitions as I will need them 
# for my analyze functions.


# # Step 2b: Design a function to read the information and store it as data in your program

# In[4]:


###########

# Functions

@typecheck
def read(filename: str) -> List[PuertoRicoSmokeData]:
    """    
    reads information from the specified file and returns the percentages of the population who 
    smoked everyday and who are former smokers in the state of Puerto Rico over various years
    """
    # loprsd contains the result so far
    loprsd = [] # type: List[PuertoRicoSmokeData]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line
         
        for row in reader:
            smoke_everyday_percentage = parse_float(row[2].rstrip('%')) # needed to strip out the percentage so I can
                                                                        # use it as a float 
            former_smoker_percentage = parse_float(row[4].rstrip('%'))
            
            prsd = PuertoRicoSmokeData(parse_int(row[0]), row[1], smoke_everyday_percentage, former_smoker_percentage)
            loprsd.append(prsd)
    
    return loprsd

# Begin testing
start_testing()

# Examples and tests for read
expect(read("tobacco_test1.csv"), [PuertoRicoSmokeData(1996, 'Puerto Rico', 9.40, 16.0), 
                                   PuertoRicoSmokeData(1997, 'Puerto Rico', 9.40, 15.7), 
                                   PuertoRicoSmokeData(1998, 'Puerto Rico', 10.10, 16.8)])

expect(read("tobacco_test2.csv"), [PuertoRicoSmokeData(2009, 'Puerto Rico', 6.90, 18.0), 
                                   PuertoRicoSmokeData(2010, 'Puerto Rico', 7.50, 17.3)])

# show testing summary
summary()


# # Step 2c: Design functions to analyze the data

# In[5]:


@typecheck
def main(fn: str) -> None:
    """
    Reads the file from given filename and returns a line graph of the
    smoking everyday data (blue line) vs former smoker (red line) over the years for the state of Puerto Rico
    """
    # template as a function composition
    return plot_years_smoke_everyday(read(fn))


@typecheck
def is_puerto_rico(state: str) -> bool:
    '''
    returns True if the state is Puerto Rico, otherwise False
    '''
    
    # return True # body of the stub
    # return ...(state) # template based on atomic distinct #????
    
    return state == "Puerto Rico"
    
@typecheck
def get_smoke_everyday(smoke_data: List[PuertoRicoSmokeData]) -> List[float]:
    '''
    returns a list of smoking everday percentages
    '''
    # return [] # body of the stub
    # template based on List[PuertoRicoSmokeEveryday]
    
    # smoking data is the list of smoking data seen so far
    smoking_data = []
    for s in smoke_data:
        if is_puerto_rico(s.state): 
            smoking_data.append(s.smoke_everyday)
    return smoking_data 

@typecheck
def smoke_everday_percent_change(smoke_data: List[PuertoRicoSmokeData]) -> str:
    '''
    returns the percentage change in smoking everday
    '''
    # return [] # body of the stub
    # template based on List[PuertoRicoSmokeEveryday]
    
    smoke_everyday = get_smoke_everyday(smoke_data)
    
    percent_change = round(smoke_everyday[0] - smoke_everyday[-1], 3)
    
    if smoke_everyday[0] > smoke_everyday[-1]:
        return "Smoking everday decreased by " + str(percent_change) + "%"
    else:
        return "Smoking everday increased by " + str(abs(percent_change)) + "%"

@typecheck
def get_former_smoker(smoke_data: List[PuertoRicoSmokeData]) -> List[float]:
    '''
    returns a list of former smoker percentages
    '''
    # return [] # body of the stub
    # template based on List[PuertoRicoSmokeEveryday]
    
    # smoking data is the list of former smoker data seen so far
    smoking_data = []
    for s in smoke_data:
        if is_puerto_rico(s.state): 
            smoking_data.append(s.former_smoker)
    return smoking_data 

@typecheck
def former_smoker_percent_change(smoke_data: List[PuertoRicoSmokeData]) -> str:
    '''
    returns the percentage change in former smokers
    '''
    # return [] # body of the stub
    # template based on List[PuertoRicoSmokeEveryday]
    
    former_smoker = get_former_smoker(smoke_data)
    
    percent_change = round(former_smoker[-1] - former_smoker[0], 3)
    
    if former_smoker[-1] > former_smoker[0]:
        return "Former smokers increased by " + str(percent_change) + "%"
    else:
        return "Former smokers decreased by " + str(percent_change) + "%"

@typecheck
def get_years(year: List[PuertoRicoSmokeData]) -> List[int]:
    '''
    returns a list of years
    '''
    # return [] # body of the stub
    # template based on List[PuertoRicoSmokeEveryday]
    
    # smoking data is the list of years seen so far
    years = []
    for y in year:
        if is_puerto_rico(y.state):
            years.append(y.year)
    return years 

@typecheck
def plot_years_smoke_everyday(loprsd: List[PuertoRicoSmokeData]) -> None:
    """
    display a line graph of the smoking everyday data (blue line) vs former smoker (red line) 
    over the years for the state of Puerto Rico
    """
    # return None # body of the stub
    
    # set the x-axis label, y-axis label, and plot title
    pyplot.xlabel('Years')
    pyplot.ylabel('Smoking (%)')
    pyplot.title('Percentage of population that Smoked Everyday vs Former Smoker in the State of Puerto Rico')
    
    # plot the data
    p1 = pyplot.plot(get_years(loprsd), get_smoke_everyday(loprsd))
    p2 = pyplot.plot(get_years(loprsd), get_former_smoker(loprsd))
    
    # set some properties for the lines, p1 and p2 
    pyplot.setp(p1, color='b', linewidth=2.0, marker="o", label="Smoke Everday (%)")
    pyplot.setp(p2, color='r', linewidth=2.0, marker="o", label="Former Smoker (%)")
    
    pyplot.legend(bbox_to_anchor=(1.05, 1), loc=2)
    
    pyplot.show()
    
    return None


start_testing()

# tests for is_puerto_rico
expect(is_puerto_rico("Puerto Rico"), True)
expect(is_puerto_rico("Montana"), False)

# tests for get_smoke_everyday
expect(get_smoke_everyday(L0), [])
expect(get_smoke_everyday(L1), [9.4, 9.4])
expect(get_smoke_everyday(L2), [9.4, 9.4, 10.1])

# tests for get_years
expect(get_years(L0), [])
expect(get_years(L1), [1996, 1997])
expect(get_years(L2), [1996, 1997, 1998])

# tests for get_former_smoker
expect(get_former_smoker(L0), [])
expect(get_former_smoker(L1), [16.0, 15.7])
expect(get_former_smoker(L2), [16.0, 15.7, 16.8])

# tests for smoke_everday_percent_change 
expect(smoke_everday_percent_change(read('tobacco.csv')), 'Smoking everday decreased by 1.9%')
expect(smoke_everday_percent_change(L1), 'Smoking everday increased by 0.0%')
expect(smoke_everday_percent_change(L2), 'Smoking everday increased by 0.7%')

# tests for former_smoker_percent_change 
expect(former_smoker_percent_change(read('tobacco.csv')), 'Former smokers increased by 1.3%')
expect(former_smoker_percent_change(L1), 'Former smokers decreased by -0.3%')
expect(former_smoker_percent_change(L2), 'Former smokers increased by 0.8%')

# tests for plot_years_smoke_everyday
expect(plot_years_smoke_everyday(L2), None)

# tests for main
expect(main('tobacco.csv'), None)

summary()


# plot_years_smoke_everyday(read('tobacco.csv'))
smoke_everday_percent_change(read('tobacco.csv'))
# former_smoker_percent_change(read('tobacco.csv'))
# main('tobacco.csv')

