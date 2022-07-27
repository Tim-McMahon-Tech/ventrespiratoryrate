# This equation is in NO WAY to be implemented in a medical setting. It is merely for EDUCATIONAL PURPOSES ONLY.
# This script will give you a desired respiratory rate to adjust your ventilator following the initation of mechanical ventilation.
# It is only to be used as a guideline (educational purposes only).

# ABG: 7.18,  PCO2 75, PaO2 90, HCO3 32, SaO2 95.

# This variable is the current respiratory rate set on the ventilator.
var1 = 12


# This variable is the current PCO2 from the arterial blood gas results.
var2 = 75


# This variable is the desired or targeted PCO2. In this case, 45 ("normal" PCO2)
var3 = 45


res = var1 * var2 / var3


print(res)

# res  = 20.0 
# res = the desired adequate value to adjust the respiratory rate to is 20. 

# Repeat ABG: 7.36, PCO2 45, PaO2 90, HCO2 27, SaO2 95
