# Plantilla para el preprocesado de Datos - Datos Faltantes
# Importar el Dataset

dataset = read.csv('Data.csv')

# Tratamiento de los valores NA

dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), 
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean (x, na.rm = TRUE)),
                        dataset$Salary)