var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://fruityvice.com/api/fruit/kiwi");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());