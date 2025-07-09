(async () => {
  const username = document.querySelector('meta[name="user-login"]').content;
  const getUsers = async (type) => {
    let users = [];
    let page = 1;
    while (true) {
      const res = await fetch(`https://github.com/${username}?page=${page}&tab=${type}`);
      const text = await res.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'text/html');
      const items = [...doc.querySelectorAll('span.Link--secondary.pl-1')].map(el =>
        el.textContent.trim()
      );
      if (items.length === 0) break;
      users.push(...items);
      page++;
    }
    return users;
  };

  console.log("Buscando quem você segue...");
  const following = await getUsers('following');
  console.log(`Você segue ${following.length} pessoas.`);

  console.log("Buscando seus seguidores...");
  const followers = await getUsers('followers');
  console.log(`Você tem ${followers.length} seguidores.`);

  const notFollowingBack = following.filter(user => !followers.includes(user));

  console.log(`\nPessoas que você segue e que NÃO te seguem de volta: (${notFollowingBack.length})`);
  console.log(notFollowingBack.join('\n') || 'Todos te seguem de volta 👌');
})();
