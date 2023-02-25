import controller as cr
import UI as ui
operation = '1'
while (operation != '0'):
    ui.prompt()
    operation = cr.get_operation_number()
    cr.perform_operation(operation)