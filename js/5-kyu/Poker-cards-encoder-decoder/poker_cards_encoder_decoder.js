const cards = 'A23456789TJQK'
const cardSuits = 'cdhs'
const cardsWeight =  cards.length

function getSuitWeight(suit) {
    return cardSuits.indexOf(suit) * cardsWeight
}

function ascendingSort(array) {
    return array.sort( (a,b ) => a - b)
}

function encode (input) {
    return ascendingSort(input.map(card => card.split(''))
        .map( ([card, suit]) => getSuitWeight(suit) + cards.indexOf(card)))
}

function decodeCard(cardWeight) {
    suit = cardSuits[Math.floor(cardWeight / cardsWeight)]
    card = cards[cardWeight - getSuitWeight(suit)]
    return card + suit
}

function decode (input) {
    return ascendingSort(input)
        .map( cardWeight => decodeCard(cardWeight) )
}
