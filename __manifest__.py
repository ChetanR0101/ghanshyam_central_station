{
    'name' : "FuelStation",
    'version' : "1.0",
    'author' : "ghanshyam",
    'summary': "Fuel Station Management",
    'description': "Fuel Station",
    'depends' : ['base'],
    'data' : ['views/fuel_station_view.xml',
              'views/fuel_stock.xml',
              'views/fuel_details_view.xml',
              'views/fuel_inventory_record_in_view.xml',
              'views/fuel_inventory_record_out_view.xml',
              'views/fuel_inventory_transaction_in_view.xml',
              'views/fuel_inventory_transaction_out_view.xml',
              'views/fuel_tanker_view.xml',
              'security/ir.model.access.csv',
              'security/security.xml',
            ],
    'installable' : True,   
    'application' : True,
}
