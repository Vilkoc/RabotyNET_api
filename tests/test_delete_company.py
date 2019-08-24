
def test_delete_company(app):
    app.authentication("cowner@gmail.com", "cowner")
    company_presence = app.get("http://localhost:8080/RabotyNET/companies/exists/InventorSoft")
    assert company_presence.text == "true"
    app.delete("http://localhost:8080/RabotyNET/companies/delete/2")
    company_absence = app.get("http://localhost:8080/RabotyNET/companies/exists/InventorSoft")
    assert company_absence.status_code == 200
    assert company_absence.text == "false"