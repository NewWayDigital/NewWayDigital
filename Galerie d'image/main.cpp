#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;
string n;
class Galerie
{
private:
    struct Image
    {
        string Nom_du_fichier;
        string description;
        string categorie;
        vector <string> tags;
    };

    vector <Image> images;

public:

    void addImage()
    {
        string Nom_du_fichier, description, categorie, tagsInput;
        vector <string> tags;

        cout << "Entrez le nom du fichier de l'image : ";
        cin.ignore();
        getline(cin, Nom_du_fichier);

        cout << "Entrez la description de l'image : ";
        getline(cin, description); //

        cout << "Entrez la categorie de l'image (nature, portraits, architecture, etc.) : ";
        getline(cin, categorie);

        cout << "Entrez les etiquettes (tags) de l'image (separees par des espaces) : ";
        getline(cin, tagsInput);

        istringstream iss(tagsInput);
        string tag;

        while (iss >> tag)
        {
            tags.push_back(tag);
        }

        images.push_back({Nom_du_fichier, description, categorie, tags});
        cout << " __________________________________"<< endl;
        cout << "|    Image ajoutee avec succes     |"<< endl;
        cout << "|__________________________________|"<< endl;
    }

    void listImages()
    const
    {
        if (images.empty())
        {
            cout << "La galerie est vide.\n";
            return;
        }
        cout << " ________________________ "<< endl;
        cout << "|    Liste des images    |"<< endl;
        cout << "|________________________|"<< endl;

        for (size_t i = 0; i < images.size(); ++i)
        {
            const Image& img = images[i];
            cout << i + 1 << ". " << img.Nom_du_fichier << " - " << img.description << " - Catégorie : " << img.categorie << " - Tags : ";
            for (const auto& tag : img.tags)
            {
                cout << tag << " ";
            }
            cout << '\n';
        }
    }

    void showImage()
    const
    {
        if (images.empty())
        {
            cout << "La galerie est vide.\n";
            return;
        }
        else
        {
        cout<<"Entrez le nom de l'image"<<endl;
        cin>>n;
      //Affiche une image.
        for(int i(0);i<images.size();++i){
        if(images[i].Nom_du_fichier == n){
            cout<<"Nom: "<<images[i].Nom_du_fichier<<endl;
    cout<<"Description: "<<images[i].description<<endl;
    cout<<"Categorie: "<<images[i].categorie<<endl;
    cout<<endl;
        }else if(i == images.size()-1){
            cout<<"Cette image n'est pas dans votre liste."<<endl;}
            }
} }

    void deleteImage()
    {
        if (images.empty())
        {
            cout << "La galerie est vide.\n";
            return;
        }
        size_t index;
        cout << "Entrez le numéro de l'image à supprimer : ";
        cin >> index;

        if (index > 0 && index <= images.size())
        {
            cout << "Image supprimee : " << images[index - 1].Nom_du_fichier << '\n';
            images.erase(images.begin() + (index - 1));
            cout << " ____________________________________"<< endl;
            cout << "|    Image supprimée avec succes     |"<< endl;
            cout << "|____________________________________|"<< endl;
        }
        else
        {
            cout << "Index invalide.\n";
        }
    }

    void modifyImage()
    {
        if (images.empty())
        {
            cout << " __________________________"<< endl;
            cout << "|   La galerie est vide    |"<< endl;
            cout << "|__________________________|"<< endl;
            return;
        }

        size_t index;
        cout << "Entrez le numéro de l'image à modifier : ";
        cin >> index;

        if (index > 0 && index <= images.size())
        {
            Image& img = images[index - 1];
            cout << "Entrez le nouveau nom du fichier de l'image : ";
            cin.ignore();
            getline(cin, img.Nom_du_fichier);

            cout << "Entrez la nouvelle description de l'image : ";
            getline(cin, img.description);

            cout << "Entrez la nouvelle catégorie de l'image : ";
            getline(cin, img.categorie);

            string tagsInput;
            cout << "Entrez les nouveaux tags de l'image (séparés par des espaces) : ";
            getline(cin, tagsInput);

            istringstream iss(tagsInput);
            img.tags.clear();
            string tag;

            while (iss >> tag)
            {
                img.tags.push_back(tag);
            }
            cout << " _________________________________ "<< endl;
            cout << "|    Image modifiée avec succès   |"<< endl;
            cout << "|_________________________________|"<< endl;
        }

        else
        {
            cout << " _______________________ "<< endl;
            cout << "|     Index invalide    |"<< endl;
            cout << "|_______________________|"<< endl;
        }
    }

    void displayMenu() const
    {
        cout << " __________________________"<< endl;
        cout << "|     Galerie d'Images     |"<< endl;
        cout << "|__________________________|"<< endl;
        cout << "|" << endl;
        cout << "|--> 1. Ajouter une image\n";
        cout << "|" << endl;
        cout << "|--> 2. Afficher la liste des images\n";
        cout << "|" << endl;
        cout << "|--> 3. Afficher une image specifique\n";
        cout << "|" << endl;
        cout << "|--> 4. Supprimer une image\n";
        cout << "|" << endl;
        cout << "|--> 5. Modifier une image\n";
        cout << "|" << endl;
        cout << "|--> 6. Organiser une image\n";
        cout << "|" << endl;
        cout << "|--> 7. Quitter\n";
        cout << " __________________________"<< endl;
        cout << "|  Choisissez une option   |"<< endl;
        cout << "|__________________________|"<< endl;
    }

    void Organiser(){
        if (images.empty())
        {
            cout << "La galerie est vide.\n";
            return;
        }else{
for(int i(0);i<images.size();++i){
        if(images[i].categorie == "nature"){
    cout<<"Nom: "<<images[i].Nom_du_fichier<<endl;
    cout<<"Description: "<<images[i].description<<endl;
    cout<<"Categorie: "<<images[i].categorie<<endl;
    cout<<endl;
        }else{}}
        for(int i(0);i<images.size();++i){
        if(images[i].categorie == "portraits"){
    cout<<"Nom: "<<images[i].Nom_du_fichier<<endl;
    cout<<"Description: "<<images[i].description<<endl;
    cout<<"Categorie: "<<images[i].categorie<<endl;
    cout<<endl;
        }else{}}
        for(int i(0);i<images.size();++i){
        if(images[i].categorie == "architecture"){
    cout<<"Nom: "<<images[i].Nom_du_fichier<<endl;
    cout<<"Description: "<<images[i].description<<endl;
    cout<<"Categorie: "<<images[i].categorie<<endl;
    cout<<endl;
        }else{}} } }

    void run()
    {
        int choice;

        do {
            displayMenu();
            std::cin >> choice;

            switch (choice)
            {
                case 1:
                    addImage();
                    break;
                case 2:
                    listImages();
                    break;
                case 3:
                    showImage();
                    break;
                case 4:
                    deleteImage();
                    break;
                case 5:
                    modifyImage();
                    break;
                case 6:
                    Organiser();
                    break;
                case 7:
                    cout << " ________________"<< endl;
                    cout << "|   Au revoir!   |"<< endl;
                    cout << "|________________|"<< endl;
                    break;
                default:
                    cout << " __________________________________________ "<< endl;
                    cout << "|    Choix invalide, veuillez reessayer    |"<< endl;
                    cout << "|__________________________________________|"<< endl;
            }
        }
         while (choice != 7);
    }
};

int main()
{
    Galerie galerie;

    galerie.run();

    return 0;
}
