import json_manager
import click

@click.group()
def cli():
    pass

#Crea usuario
@cli.command()
@click.option('--name', required=True, help="Nombre del usuario")
@click.option('--lastname', required=True, help="Apellido del usuario")
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('Nombre y apellido son requeridos')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user ={
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"Usario {name} {lastname} creado con el id {new_id}")

#Ejecuta la funcion de lectura importada y lo recorre    
@cli.command()
def users():    
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

#Agrega usuario
@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None) #Me dará el usuario o nada si no encuentra
    if user is None:
        print(f"El usuario con id {id} no se encuentra")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")
        
#Actualizar
@cli.command()
@click.argument('id', type=int)
@click.option('--name', help="Nombre del usuario")
@click.option('--lastname', help="Apellido del usuario")
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f"Usuario con id {id} actualizado correctamente")
        
#Elimina usuario
@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None) #Me dará el usuario o nada si no encuentra
    if user is None:
        print(f"El usuario con id {id} no se encuentra")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"El usuario con id {id} a sido eliminado")
        
if __name__ == '__main__':
    cli()
    

    