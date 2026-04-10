import os

files = ['o-nas.html', 'skup-samochodow.html', 'laweta-pomoc-drogowa.html', 'kontakt.html']

search_block = """                <nav>
                    <ul>
                        <li><a href="index.html">STRONA GŁÓWNA</a></li>
                        <li><a href="o-nas.html">O NAS</a></li>
                        <li><a href="skup-samochodow.html">SKUP SAMOCHODÓW</a></li>
                        <li><a href="laweta-pomoc-drogowa.html">POMOC DROGOWA</a></li>
                        <li><a href="kontakt.html">KONTAKT</a></li>
                    </ul>
                <div class="header-cta">
                    <a href="tel:+48730035559" class="btn-call">
                        <i class="fas fa-phone-alt"></i>
                        <span>
                            <span class="btn-label">SKUP SAMOCHODÓW</span>
                            <span class="btn-number">730 035 559</span>
                        </span>
                    </a>
                    <a href="tel:+48790676446" class="btn-call">
                        <i class="fas fa-phone-alt"></i>
                        <span>
                            <span class="btn-label">POMOC DROGOWA</span>
                            <span class="btn-number">790 676 446</span>
                        </span>
                    </a>
                </div>
                </nav>"""

replace_block = """                <nav>
                    <ul>
                        <li><a href="index.html">STRONA GŁÓWNA</a></li>
                        <li><a href="o-nas.html">O NAS</a></li>
                        <li><a href="skup-samochodow.html">SKUP SAMOCHODÓW</a></li>
                        <li><a href="laweta-pomoc-drogowa.html">POMOC DROGOWA</a></li>
                        <li><a href="kontakt.html">KONTAKT</a></li>
                    </ul>
                    <div class="header-cta mobile-only">
                        <a href="tel:+48730035559" class="btn-call">
                            <i class="fas fa-phone-alt"></i>
                            <span>
                                <span class="btn-label">SKUP SAMOCHODÓW</span>
                                <span class="btn-number">730 035 559</span>
                            </span>
                        </a>
                        <a href="tel:+48790676446" class="btn-call">
                            <i class="fas fa-phone-alt"></i>
                            <span>
                                <span class="btn-label">POMOC DROGOWA</span>
                                <span class="btn-number">790 676 446</span>
                            </span>
                        </a>
                    </div>
                </nav>
                <div class="header-cta desktop-only">
                    <a href="tel:+48730035559" class="btn-call">
                        <i class="fas fa-phone-alt"></i>
                        <span>
                            <span class="btn-label">SKUP SAMOCHODÓW</span>
                            <span class="btn-number">730 035 559</span>
                        </span>
                    </a>
                    <a href="tel:+48790676446" class="btn-call">
                        <i class="fas fa-phone-alt"></i>
                        <span>
                            <span class="btn-label">POMOC DROGOWA</span>
                            <span class="btn-number">790 676 446</span>
                        </span>
                    </a>
                </div>"""

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if search_block in content:
        new_content = content.replace(search_block, replace_block)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Search block not found in {filename}")
