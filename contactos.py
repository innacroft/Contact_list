# -*- coding: utf-8 -*-
import csv
class Contact:
    def __init__(self,name, phone,email):
        self.name=name
        self.phone=phone
        self.email=email


class ContactBook:
    def __init__(self):
        self._contacts=[]
    
    def add(self, name,phone,email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                print('--*--*--*--*--*--*--*--*')
                print('Nombre: {}'.format(contact.name))
                print('Telefono: {}'.format(contact.phone))
                print('Email: {}'.format(contact.email))       
                print('--*--*--*--*--*--*--*--*')
                break
        else:
            self.not_found()

    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                parameter= str(raw_input('''
                ¿Qué dato deseas actualizar?
                [n]ombre
                [t]elefono
                [e]mail
                [to]dos los datos: '''))
                if parameter == 'n':
                    name_= str(raw_input('Escribe el nuevo nombre del contacto: '))
                    del self._contacts[idx].name
                    self._contacts[idx].name=name_
                    self._save()
                    break
                if parameter == 't':
                    telefono_= str(raw_input('Escribe el nuevo telefono del contacto: '))
                    del self._contacts[idx].phone
                    self._contacts[idx].phone=telefono_
                    self._save()
                    break
                if parameter == 'e':
                    email_= str(raw_input('Escribe el nuevo email del contacto: '))
                    del self._contacts[idx].email
                    self._contacts[idx].email=email_
                    self._save()
                    break
                if parameter == 'to':
                    
                    name_= str(raw_input('Escribe el nuevo nombre del contacto: '))
                    telefono_= str(raw_input('Escribe el nuevo telefono del contacto: '))
                    email_= str(raw_input('Escribe el nuevo email del contacto: '))
                    del self._contacts[idx].name
                    del self._contacts[idx].phone
                    del self._contacts[idx].email
                    self._contacts[idx].name=name_
                    self._contacts[idx].phone=telefono_
                    self._contacts[idx].email=email_
                    self._save()
                    print('Usuario actualizado exitosamente!')
                    break
                else:
                    print('Comando no encontrado.')
                    break
                
        else:
            self.not_found()

    def _print_contact(self,contact):
        print('--*--*--*--*--*--*--*--*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))       
        print('--*--*--*--*--*--*--*--*')    

    def not_found(self):
        print('--*--*--*--*--*--*--*--*')
        print('Contacto no encontrado !!')
        print('--*--*--*--*--*--*--*--*')

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))
    
    
        




def run():
    contact_book= ContactBook()
    try:# intenta cargar archivo con usuarios previamente guardados
        with open('contacts.csv','r') as f:
            reader=csv.reader(f)
            for idx, row in enumerate(reader): 
                if idx==0:      #ignora el primer componente de la lista
                    continue
                contact_book.add(row[0],row[1], row[2])  #agrega todos los demas componentes d ela lista 
                
    except: # si no encuentra el archivo crea uno vacio
        with open('contacts.csv','w') as f:
            f.write('')

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name= str(raw_input('Escribe el nombre del contacto: '))
            phone= str(raw_input('Escribe el telefono del contacto: '))
            email= str(raw_input('Escribe el email del contacto: '))
            contact_book.add(name,phone,email)

        elif command == 'ac':
            name= str(raw_input('Escribe el nombre del contacto: '))
            contact_book.update(name)

        elif command == 'b':
            name= str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)
            

        elif command == 'e':
            name= str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
            

        elif command == 'l':
            
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()