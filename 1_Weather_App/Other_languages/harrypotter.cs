var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://hp-api.onrender.com/api/spells");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());