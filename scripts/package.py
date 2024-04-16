from datapackage import Package

# Creating a new package
package = Package(base_path='C:/Users/polat/Desktop/city-percentage-of-population-with-higher-education-degrees/data')
package.infer('higher_education.csv')

# Saving the package to 'datapackage.json'
package.save('../datapackage.json')
