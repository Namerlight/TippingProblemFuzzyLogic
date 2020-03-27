# Mostly from https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
# Extremely simple implementation and partly copypasted, I just did this so I could go through the code myself.

import numpy
import skfuzzy
import matplotlib.pyplot as plt
from skfuzzy import control

quality = skfuzzy.control.Antecedent(numpy.arange(0, 11, 1), 'quality')     # Antecedent = Input Variable
service = skfuzzy.control.Antecedent(numpy.arange(0, 11, 1), 'service')
tip = skfuzzy.control.Consequent(numpy.arange(0, 26, 1), 'tip')             # Consequent = Output Variable

quality.automf(3)       # 'automf' splits the range into equal intervals. 3, gives low, mid, high
service.automf(3)       # 3, 5, 7 can be used, or quality.automf(names=['bad', 'good']) for custom.

tip['low'] = skfuzzy.trimf(tip.universe, [0, 0, 13])                        # Generates the triangular graph shape
tip['medium'] = skfuzzy.trimf(tip.universe, [0, 13, 25])                    # The parameters are Left corner,
tip['high'] = skfuzzy.trimf(tip.universe, [13, 25, 25])                     # midpoint/tip, right corner respectively.

# quality.view()                                                            # View the triangular graphs for the
# service.view()                                                            # membership function of the and the
# tip.view()                                                                # outputs.

rule1 = skfuzzy.control.Rule(quality['poor'] | service['poor'], tip['low'])     # Rules
rule2 = skfuzzy.control.Rule(service['average'], tip['medium'])
rule3 = skfuzzy.control.Rule(service['good'] | quality['good'], tip['high'])

# rule1.view()                                                              # View a graphical representation of the
# rule2.view()                                                              # rules. No, I have no idea how to actually
# rule3.view()                                                              # make sense of these graphs.

tipping_ctrl = skfuzzy.control.ControlSystem([rule1, rule2, rule3])         # Creates a "control system" that
                                                                            # follows the given rules.
tipping = skfuzzy.control.ControlSystemSimulation(tipping_ctrl)             # Creates a specific object that takes
                                                                            # inputs and passes them to the control.
tipping.input['quality'] = 10.5
tipping.input['service'] = 12

tipping.compute()                                                           # Calculates the output

print(tipping.output['tip'])
tip.view(sim=tipping)                                                       # Graph for the output.
plt.show()


