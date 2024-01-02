{
  'name' : 'Task Manager',
  'version' : '1.0.0',
  'category' : 'ACC',
  'sequence': -100,
  'summary' : 'Task Manager',
  'description' : """Task Manager""",
  'depends':  ['base'],
  'data':  [

     'views/task_view.xml',
      'security/ir.model.access.csv',
   ],

  'demo':[],
  'application':  True,
  'auto_install':  False,
  'license': 'LGPL-3',
  'odoo': '17.0',
}