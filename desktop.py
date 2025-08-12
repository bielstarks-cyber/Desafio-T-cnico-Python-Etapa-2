from pywinauto import Application
from timer import kill_timer


def desk_abrir(valor2):
    app = Application(backend='uia')
    app.start('C:\\EmployeeList.exe')
    Employee = app.window(title='Employee Database')
    #Employee.print_control_identifiers()
    edit = Employee.child_window(auto_id='txtEmpId')
    edit.type_keys(valor2)
    search = Employee.child_window(auto_id='btnSearch')
    search.click()

    return app

def desk_form(app):
    lista = []
    main_window = app.window(title='Employee Database')
    campos_form = main_window.children(control_type='Edit')
    for i, celula in enumerate(campos_form):
        valor_celula = celula.get_value()
        lista.append(valor_celula)
        i=i+1


    return lista









# if __name__ == "__main__":
#     app = desk_abrir('1020')
#     desk_form()

    # texto = Employee.child_window(auto_id='txtFirstName')
    # valor_campo = texto.texts()[0]
    # print("Texto 1",valor_campo)


# edit = Employee.child_window(classname='Enter the Emp Number')
# edit.send_keys('123456')
# app.EmployeeList.send_keys(Keys.ARROW_RIGHT)
