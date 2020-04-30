#Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a marketplace for people and organizations to buy and sell pieces of art!

#In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.


#class for modeling works of art
class Art:

    #constructor for artist, title, medium, and year
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner


    def __repr__(self):
        return '{artist_name}. "{title}". {year}, {medium}. {owner_name}, {owner_location}.'.format(artist_name = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)




#class to create marketplace in order to sell works of art. Includes functionality for buying, selling, listing, and delisting artworks 
class Marketplace:

    #constructor for listings that is empty list when marketplace is created
    def __init__(self):
        self.listings = []


    #method for adding a new listing to the marketplace listings
    def add_listing(self, new_listing):
        return self.listings.append(new_listing)


    #method for removing a listing from the marketplace
    def remove_listing(self, deleted_listing):
        self.listings.pop(self.listings.index(deleted_listing))


    #method to show the available listings
    def show_listings(self):
        for x in self.listings:
            print(x)




#class for clients 
class Client:
    
    #constructor for name, location, and determining if client is a museum or not
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.location = location
        self.is_museum = is_museum
        self.wallet = wallet


    #method for selling artwork 
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)
        else:
            print('{name} is not the owner of {artwork_title}.'.format(name = self.name, artwork_title = artwork.title))


    #method for buying artwork
    def buy_artwork(self, artwork):
        
        #test to see if client is owner of the artwork
        if artwork.owner != self:

            #iterate through listing to search for selected artwork
            for x in veneer.listings:
                if artwork == x.artwork:
                    if self.wallet >= x.price:
                        self.wallet = self.wallet - x.price
                        x.artwork.owner = self
                        print('{client_name} is now the owner of {artwork_title}'.format(client_name = self.name, artwork_title = x.artwork.title))
                        veneer.remove_listing(x)
                    else:
                        print('{client_name} does not have enough in their wallet to buy {artwork_title}.'.format(client_name = self.name, artwork_title = x.artwork.title))
            
            #if artwork not in listing, will print the following:
            print('{artwork_title} is not in the Veneer Marketplace.'.format(artwork_title = artwork.title))
        
        #if client is the owner of the artwork, will print the following:
        else:
            print('{client_name} already owns the {artwork_title}'.format(client_name = self.name, artwork_title = artwork.title))



#class for listing works of art
class Listing:
    
    #constructor for piece of artwork being listed, price of the art, and instance of Client class
    def __init__(self, artwork, price, seller):
        self.artwork = artwork
        self.price = price
        self.seller = self.artwork.owner


    #string representation describing the name of piece of art and price of the work of art
    def __repr__(self):
        return '{name_art}: {price}'.format(name_art = self.artwork.title, price = self.price)






#instantiation of the veneer marketplace
veneer = Marketplace()

#testing show listings method
veneer.show_listings()

#instantiation of the edytta client
edytta = Client('Edytta Halpirt', 'Private Collection', False, 0)

#instantiation of moma client
moma = Client('The MOMA', 'New York', True, 6000000)

#instantiation of girl with mandolin artwork
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)

#instantiation of mona lisa
mona_lisa = Art('Someone', 'Mona Lisa', 'something', 1999, edytta)

#test string representation of girl with mandolin
print(girl_with_mandolin)

#edytta wants to sell artwork and lists on veneer marketplace
edytta.sell_artwork(girl_with_mandolin, 5000000)

#test to show the addition of artwork
veneer.show_listings()

#moma client buys girl with mandolin from edytta
moma.buy_artwork(girl_with_mandolin)

#test to show removal of artwork from listing
veneer.show_listings()

#test to show new owner of artwork
print(girl_with_mandolin)

#test to show that client cannot buy artwork that is not on the veneer marketplace
moma.buy_artwork(mona_lisa)

#test wallet reduction after purchase
print(moma.wallet)

#additional functionality
# • Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
# • Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
# • Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.