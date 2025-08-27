from typing import Dict, Optional

# Complete book summaries dictionary
book_summaries_dict = {
    "1984": (
        "Romanul lui George Orwell descrie o societate distopică aflată sub controlul total al statului. "
        "Oamenii sunt supravegheați constant de 'Big Brother', iar gândirea liberă este considerată crimă. "
        "Winston Smith, personajul principal, încearcă să reziste acestui regim opresiv prin căutarea adevărului și libertății. "
        "Este o poveste despre libertate, adevăr și manipulare ideologică, explorând temele controlului guvernamental și rezistenței individuale."
    ),
    "The Hobbit": (
        "Bilbo Baggins, un hobbit confortabil și fără aventuri, este luat prin surprindere "
        "atunci când este invitat într-o misiune de a recupera comoara piticilor păzită de dragonul Smaug. "
        "Pe parcursul călătoriei, el descoperă curajul și resursele interioare pe care nu știa că le are. "
        "Povestea este plină de creaturi fantastice, prietenii neașteptate și momente tensionate. "
        "Temele principale includ aventura, creșterea personală și descoperirea propriei valori."
    ),
    "To Kill a Mockingbird": (
        "Situat în Alabama anilor 1930, romanul urmărește-o pe Scout Finch care învață despre dreptate, "
        "moralitate și prejudecăți prin apărarea tatălui ei a unui bărbat de culoare acuzat fals de viol. "
        "Atticus Finch devine un simbol al integrității morale în fața presiunii sociale. "
        "Cartea explorează temele injustiției rasiale, curajului moral și pierderii inocenței copilăriei."
    ),
    "The Great Gatsby": (
        "Capodopera lui F. Scott Fitzgerald despre urmărirea obsesivă a lui Jay Gatsby pentru Daisy Buchanan "
        "în America anilor 1920. O critică a Visului American și a decăderii morale de sub suprafața "
        "strălucitoare a Epocii Jazz-ului. Gatsby organizează petreceri extravagante în speranța de a o recâștiga pe Daisy. "
        "Temele includ iubirea, bogăția, corupția și imposibilitatea de a recăpăta trecutul."
    ),
    "Harry Potter and the Sorcerer's Stone": (
        "Harry Potter descoperă că este un vrăjitor în ziua de 11 ani și intră la Școala de Vrăjitorie și Magie Hogwarts. "
        "Învață despre trecutul său tragic, își face prieteni pe viață și se confruntă cu vrăjitorul întuneric care i-a ucis părinții. "
        "Alături de Hermione și Ron, Harry descoperă secretele din castelul Hogwarts și se confruntă cu Voldemort. "
        "Temele principale sunt prietenia, magia, lupta dintre bine și rău și procesul de maturizare."
    ),
    "Pride and Prejudice": (
        "Elizabeth Bennet navighează în iubire, așteptările familiale și clasa socială în Anglia Regency. "
        "Relația ei cu mândrul domnul Darcy evoluează de la antipatia inițială la înțelegere profundă și iubire. "
        "Jane Austen critică convențiile sociale și explorează temele căsătoriei, clasei sociale și creșterii personale. "
        "Caracterizările spirituale și dialogurile inteligente fac din aceasta o operă clasică atemporală."
    ),
    "The Lord of the Rings: The Fellowship of the Ring": (
        "Frodo Baggins moștenește un inel puternic și trebuie să-l distrugă pentru a salva Middle-earth de "
        "Întunericul Sauron. Începe o călătorie epică cu o frăție de companioni care îl protejează și îl ghidează. "
        "Călătoria este plină de pericole, sacrificii și momente de curaj extraordinar. "
        "Temele includ prietenia, sacrificiul, lupta dintre bine și rău și povara responsabilității."
    ),
    "Dune": (
        "Paul Atreides devine prins într-o luptă pentru controlul planetei deșertice Arrakis, sursa valoroasei "
        "mirodenii melange. O poveste complexă de politică, religie și ecologie într-un viitor îndepărtat. "
        "Paul dezvoltă puteri presciente și devine liderul poporului Fremen în lupta împotriva opresiunii. "
        "Temele includ puterea, profeția, problemele de mediu și intrigile politice."
    ),
    "The Catcher in the Rye": (
        "Holden Caulfield, un adolescent tulburat, rătăcește prin New York City după ce este dat afară din "
        "școala pregătitoare. Narațiunea sa dezvăluie lupta cu depresia, înstrăinarea și falsitatea pe care o "
        "percepe în societatea adulților. Holden caută autenticitatea într-o lume pe care o consideră plină de ipocrizie. "
        "Temele includ alienarea, identitatea, pierderea inocenței și sănătatea mentală."
    ),
    "Brave New World": (
        "Viziunea lui Aldous Huxley despre o societate viitoare unde oamenii sunt modificați genetic și "
        "condiționați pentru roluri specifice. Bernard Marx pune la îndoială această lume aparent perfectă "
        "controlată de plăcere și droguri. Romanul explorează prețul fericirii artificiale și pierderea individualității. "
        "Temele includ controlul social, tehnologia, individualitatea și costul fericirii."
    ),
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe": (
        "Patru copii descoperă țara magică Narnia printr-un dulap și îl ajută pe leul Aslan să învingă "
        "Vrăjitoarea Albă. O poveste despre curaj, răscumpărare și triumful binelui asupra răului. "
        "Copiii învață despre sacrificiu, loialitate și puterea credinței în timpul aventurii lor magice. "
        "Temele includ magia, sacrificiul, răscumpărarea și puterea credinței."
    ),
    "One Hundred Years of Solitude": (
        "Capodopera realismului magic a lui Gabriel García Márquez urmărind șapte generații ale familiei "
        "Buendía în orașul fictiv Macondo. O țesătură bogată de iubire, pierdere și istoria Americii Latine. "
        "Romanul îmbină elementele magice cu realitatea crudă, creând o cronică unică a condiției umane. "
        "Temele includ solitudinea, ciclurile familiale, realismul magic și trecerea timpului."
    )
}


def get_summary_by_title(title: str) -> str:
    """
    Tool function to get detailed book summary by exact title.
    This function will be registered as an OpenAI function calling tool.

    Args:
        title (str): Exact title of the book

    Returns:
        str: Detailed summary of the book or error message if not found
    """
    if title in book_summaries_dict:
        return book_summaries_dict[title]
    else:
        # Try case-insensitive search
        for book_title, summary in book_summaries_dict.items():
            if book_title.lower() == title.lower():
                return summary

        available_titles = ", ".join(book_summaries_dict.keys())
        return f"Cartea '{title}' nu a fost găsită în baza de date. Cărțile disponibile sunt: {available_titles}"


# Tool definition for OpenAI function calling
get_summary_tool_definition = {
    "type": "function",
    "function": {
        "name": "get_summary_by_title",
        "description": "Get detailed summary for a specific book by its exact title",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The exact title of the book to get summary for"
                }
            },
            "required": ["title"]
        }
    }
}


def filter_inappropriate_language(text: str) -> tuple[bool, str]:
    """
    Simple content filter for inappropriate language.

    Args:
        text (str): User input text

    Returns:
        tuple[bool, str]: (is_appropriate, filtered_message)
    """
    inappropriate_words = [
        # Add Romanian and English inappropriate words
        'prost', 'idiot', 'stupid', 'fuck', 'shit', 'damn'
    ]

    text_lower = text.lower()
    for word in inappropriate_words:
        if word in text_lower:
            return False, "Îmi pare rău, dar nu pot răspunde la mesaje care conțin limbaj nepotrivit. Te rog să reformulezi întrebarea într-un mod respectuos."

    return True, text